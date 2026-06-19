import sys
import time
from pathlib import Path

try:
    import chromadb
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("Missing deps. Run: pip install -r spike/requirements.txt")
    sys.exit(1)

from app.config import (
    CHROMA_DIR,
    COLLECTION,
    CORPUS_DIR,
    EMBED_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K,
    MAX_CHUNKS_PER_DOC,
)

# ── STEP 1: LOAD CORPUS ──────────────────────────────────────────────────────

def load_corpus(corpus_dir: Path) -> list[dict]:
    docs = []
    md_files = sorted(corpus_dir.glob("*.md"))
    if not md_files:
        print(f"[ERROR] No .md files in {corpus_dir}/ — run scraper.py first")
        sys.exit(1)
    for path in md_files:
        text = path.read_text(encoding="utf-8")
        doc_id = path.stem
        title = doc_id
        for line in text.splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                break
        docs.append({"doc_id": doc_id, "title": title, "text": text})
    print(f"[LOAD] {len(docs)} documents")
    for d in docs:
        print(f"       {d['doc_id']:<40} {len(d['text']):>8,} chars")
    return docs


# ── STEP 2: RECURSIVE CHUNKING ───────────────────────────────────────────────

def recursive_split(text: str, size: int, overlap: int) -> list[str]:
    """
    Split on paragraph → newline → space in that order.
    Each split respects the size limit; falls back to hard cut only when needed.
    """
    separators = ["\n\n", "\n", " "]

    def _split(t: str, seps: list[str]) -> list[str]:
        if len(t) <= size:
            return [t] if t.strip() else []
        sep = seps[0] if seps else ""
        if not sep:
            # Hard cut fallback
            return [t[i:i+size] for i in range(0, len(t), size - overlap)]
        parts = t.split(sep)
        chunks, current = [], ""
        for part in parts:
            candidate = current + (sep if current else "") + part
            if len(candidate) <= size:
                current = candidate
            else:
                if current.strip():
                    chunks.append(current.strip())
                # If part itself is too big, recurse with next separator
                if len(part) > size:
                    chunks.extend(_split(part, seps[1:]))
                    current = ""
                else:
                    current = part
        if current.strip():
            chunks.append(current.strip())
        return chunks

    raw_chunks = _split(text, separators)

    # Apply overlap by stitching tail of previous chunk onto head of next
    if overlap == 0 or len(raw_chunks) <= 1:
        return raw_chunks
    overlapped = [raw_chunks[0]]
    for i in range(1, len(raw_chunks)):
        tail = raw_chunks[i-1][-overlap:]
        overlapped.append(tail + " " + raw_chunks[i])
    return overlapped


def chunk_docs(docs: list[dict]) -> list[dict]:
    chunks = []
    skipped_docs = []
    for doc in docs:
        doc_chunks = recursive_split(doc["text"], CHUNK_SIZE, CHUNK_OVERLAP)
        # Cap per-doc chunks so one giant file doesn't dominate the index
        if len(doc_chunks) > MAX_CHUNKS_PER_DOC:
            print(f"  [CAP] {doc['doc_id']}: {len(doc_chunks)} → {MAX_CHUNKS_PER_DOC} chunks")
            doc_chunks = doc_chunks[:MAX_CHUNKS_PER_DOC]
        if not doc_chunks:
            skipped_docs.append(doc["doc_id"])
            continue
        for i, text in enumerate(doc_chunks):
            chunks.append({
                "chunk_id": f"{doc['doc_id']}_chunk_{i}",
                "doc_id":   doc["doc_id"],
                "title":    doc["title"],
                "text":     text,
            })
    if skipped_docs:
        print(f"  [WARN] Empty after chunking: {skipped_docs}")
    print(f"[CHUNK] {len(chunks)} chunks total "
          f"(size={CHUNK_SIZE}, overlap={CHUNK_OVERLAP}, cap={MAX_CHUNKS_PER_DOC}/doc)")
    return chunks


# ── STEP 3: EMBED + INDEX ────────────────────────────────────────────────────

def build_index(chunks: list[dict]):
    print(f"[EMBED] Loading {EMBED_MODEL} ...")
    model = SentenceTransformer(EMBED_MODEL)
    
    chroma_path = Path(CHROMA_DIR)
    chroma_path.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(chroma_path))

    existing = [c.name for c in client.list_collections()]
    if COLLECTION in existing:
        col = client.get_collection(COLLECTION)
        if col.count() == len(chunks):
            print(f"[EMBED] Cache hit ({col.count()} chunks)")
            return col, model
        client.delete_collection(COLLECTION)

    col = client.create_collection(COLLECTION, metadata={"hnsw:space": "cosine"})
    print(f"[EMBED] Indexing {len(chunks)} chunks...")
    t0 = time.time()

    BATCH = 64
    all_embeddings = []
    texts     = [c["text"]     for c in chunks]
    ids       = [c["chunk_id"] for c in chunks]
    metadatas = [{"doc_id": c["doc_id"], "title": c["title"]} for c in chunks]

    for i in range(0, len(texts), BATCH):
        embs = model.encode(texts[i:i+BATCH], show_progress_bar=False).tolist()
        all_embeddings.extend(embs)

    col.upsert(ids=ids, embeddings=all_embeddings, documents=texts, metadatas=metadatas)
    print(f"[EMBED] Done in {time.time()-t0:.1f}s")
    return col, model


# ── STEP 4: RETRIEVE ─────────────────────────────────────────────────────────

def retrieve(query: str, col, model) -> list[dict]:
    # Query expansion: domain prefix improves MiniLM relevance for short queries
    expanded = f"Linear documentation: {query}"
    q_emb = model.encode([expanded]).tolist()
    results = col.query(
        query_embeddings=q_emb,
        n_results=TOP_K,
        include=["documents", "metadatas", "distances"],
    )
    hits = []
    if not results.get("ids") or not results["ids"][0]:
        return hits
        
    for i in range(len(results["ids"][0])):
        hits.append({
            "chunk_id": results["ids"][0][i],
            "doc_id":   results["metadatas"][0][i]["doc_id"],
            "title":    results["metadatas"][0][i]["title"],
            "text":     results["documents"][0][i],
            "score":    round(1 - results["distances"][0][i], 4),
        })
    return hits


# ── STEP 5: TEMPORARY DIAGNOSTIC RUNNER ──────────────────────────────────────

if __name__ == "__main__":
    print("Executing retrieve.py isolated text runner...")
    docs = load_corpus(CORPUS_DIR)
    chunks = chunk_docs(docs)
    collection, model = build_index(chunks)

    print()
    results = retrieve(
        "How do I configure workflows?",
        collection,
        model
    )

    print(f"Retrieved {len(results)} chunks\n")
    for r in results:
        print(f"{r['doc_id']:<30} score={r['score']}")