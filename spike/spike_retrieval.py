# spike/spike_retrieval.py  v2
# Fixes applied vs v1:
#   1. top-k raised 4 → 6
#   2. Max chunks per doc capped at 15 (stops one huge doc flooding the index)
#   3. Recursive character chunking (splits on \n\n → \n → " ") instead of
#      blind fixed-window — keeps semantic units together
#   4. Query expansion: prepend "Linear app:" to every query so the embedder
#      knows the domain (helps when doc text says "Linear" but query doesn't)

import os
import sys
import time
import json
import re
from pathlib import Path
from datetime import datetime

try:
    import chromadb
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("Missing deps. Run:  pip install -r spike/requirements.txt")
    sys.exit(1)

# ── CONFIG ───────────────────────────────────────────────────────────────────
CORPUS_DIR    = Path("corpus")
CHROMA_DIR    = Path("spike/.chroma_cache_v2")   # new dir so v1 cache doesn't interfere
COLLECTION    = "northwind_spike_v2"
EMBED_MODEL   = "all-MiniLM-L6-v2"
CHUNK_SIZE    = 800          # smaller chunks → more precise retrieval
CHUNK_OVERLAP = 150
TOP_K         = 6            # was 4
MAX_CHUNKS_PER_DOC = 15      # cap so one giant file can't flood the index
FINDINGS_OUT  = Path("FINDINGS.md")

# ── 10 GOLDEN QUESTIONS ──────────────────────────────────────────────────────
GOLDEN_QUESTIONS = [
    {
        "id": "q01",
        "question": "What is the conceptual model used by Linear?",
        "expected_docs": ["conceptual-model"],
        "flavor": "easy",
    },
    {
        "id": "q02",
        "question": "How do I configure workflows in Linear?",
        "expected_docs": ["configuring-workflows"],
        "flavor": "easy",
    },
    {
        "id": "q03",
        "question": "How are projects different from teams in Linear?",
        "expected_docs": ["projects", "teams"],
        "flavor": "multi_hop",
    },
    {
        "id": "q04",
        "question": "How do I triage incoming issues?",
        "expected_docs": ["triage"],
        "flavor": "easy",
    },
    {
        "id": "q05",
        "question": "How can I organize issues using labels?",
        "expected_docs": ["labels"],
        "flavor": "easy",
    },
    {
        "id": "q06",
        "question": "How do project documents work together with projects?",
        "expected_docs": ["project-documents", "projects"],
        "flavor": "multi_hop",
    },
    {
        "id": "q07",
        "question": "Can Linear be used to process payroll for employees?",
        "expected_docs": [],
        "flavor": "adversarial",
    },
    {
        "id": "q08",
        "question": "How can I filter issues using labels?",
        "expected_docs": ["filters", "labels"],
        "flavor": "multi_hop",
    },
    {
        "id": "q09",
        "question": "How do I customize display options in Linear?",
        "expected_docs": ["display-options"],
        "flavor": "easy",
    },
    {
        "id": "q10",
        "question": "How can GitHub integration help manage imported issues?",
        "expected_docs": ["github", "import-issues"],
        "flavor": "multi_hop",
    },
]


# ── STEP 1: LOAD CORPUS ──────────────────────────────────────────────────────

def load_corpus(corpus_dir: Path) -> list[dict]:
    docs = []
    md_files = sorted(corpus_dir.glob("*.md"))
    if not md_files:
        print(f"[ERROR] No .md files in {corpus_dir}/  — run scraper.py first")
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
    CHROMA_DIR.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

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
    expanded = f"Linear app support: {query}"
    q_emb = model.encode([expanded]).tolist()
    results = col.query(
        query_embeddings=q_emb,
        n_results=TOP_K,
        include=["documents", "metadatas", "distances"],
    )
    hits = []
    for i in range(len(results["ids"][0])):
        hits.append({
            "chunk_id": results["ids"][0][i],
            "doc_id":   results["metadatas"][0][i]["doc_id"],
            "title":    results["metadatas"][0][i]["title"],
            "text":     results["documents"][0][i],
            "score":    round(1 - results["distances"][0][i], 4),
        })
    return hits


# ── STEP 5: EVALUATE ─────────────────────────────────────────────────────────

def evaluate(col, model) -> list[dict]:
    rows = []
    for gq in GOLDEN_QUESTIONS:
        t0 = time.time()
        retrieved = retrieve(gq["question"], col, model)
        latency_ms = round((time.time() - t0) * 1000, 1)

        retrieved_doc_ids = [r["doc_id"] for r in retrieved]
        # Deduplicate while preserving order (for display)
        seen, unique_docs = set(), []
        for d in retrieved_doc_ids:
            if d not in seen:
                seen.add(d)
                unique_docs.append(d)

        top_score = retrieved[0]["score"] if retrieved else 0.0
        expected  = gq["expected_docs"]

        if gq["flavor"] == "adversarial":
            status = "HIT" if top_score < 0.50 else "MISS"
        else:
            found = [d for d in expected if d in retrieved_doc_ids]
            if len(found) == len(expected):
                status = "HIT"
            elif found:
                status = "PARTIAL"
            else:
                status = "MISS"

        rows.append({
            "id":             gq["id"],
            "flavor":         gq["flavor"],
            "question":       gq["question"],
            "expected_docs":  expected,
            "retrieved_docs": unique_docs,
            "top_score":      top_score,
            "top_chunk":      retrieved[0]["text"][:200] if retrieved else "",
            "status":         status,
            "latency_ms":     latency_ms,
        })
    return rows


# ── STEP 6: PRINT + SAVE ─────────────────────────────────────────────────────

ICON = {"HIT": "✅", "PARTIAL": "⚠️ ", "MISS": "❌"}

def print_table(rows):
    print("\n" + "=" * 90)
    print("SPIKE RESULTS v2 — Northwind Support Copilot · Retrieval Hit-Rate")
    print("=" * 90)
    print(f"{'ID':<5} {'Flavor':<12} {'Status':<8} {'Score':<7} {'Expected':<28} {'Retrieved (deduped)'}")
    print("-" * 90)
    for r in rows:
        exp  = ",".join(r["expected_docs"]) if r["expected_docs"] else "(none)"
        retr = ",".join(r["retrieved_docs"])
        print(f"{r['id']:<5} {r['flavor']:<12} {ICON[r['status']]} {r['status']:<6} "
              f"{r['top_score']:<7} {exp:<28} {retr}")

    hits     = sum(1 for r in rows if r["status"] == "HIT")
    partials = sum(1 for r in rows if r["status"] == "PARTIAL")
    misses   = sum(1 for r in rows if r["status"] == "MISS")
    hit_rate = round(hits / len(rows) * 100, 1)
    print("-" * 90)
    print(f"HIT: {hits}  PARTIAL: {partials}  MISS: {misses}  →  Hit-rate: {hit_rate}% ({hits}/{len(rows)})")
    print("=" * 90)
    return hits, partials, misses, hit_rate


def save_findings(rows, hits, partials, misses, hit_rate):
    lines = [
        "# FINDINGS.md — De-Risk Spike Results (v2)",
        "",
        f"> **Date:** {datetime.now().strftime('%Y-%m-%d')}  ",
        f"> **Embedding model:** `{EMBED_MODEL}`  ",
        f"> **Chunking:** recursive (size={CHUNK_SIZE}, overlap={CHUNK_OVERLAP}, cap={MAX_CHUNKS_PER_DOC}/doc)  ",
        f"> **top-k:** {TOP_K} | **Query expansion:** `Linear app support: <query>`  ",
        "",
        "## Retrieval Hit-Rate Table",
        "",
        "| ID | Flavor | Status | Top Score | Expected Doc(s) | Retrieved (deduped) |",
        "|----|--------|--------|-----------|-----------------|---------------------|",
    ]
    for r in rows:
        exp  = ", ".join(r["expected_docs"]) if r["expected_docs"] else "*(adversarial)*"
        retr = ", ".join(r["retrieved_docs"])
        lines.append(
            f"| {r['id']} | {r['flavor']} | {ICON[r['status']]} {r['status']} "
            f"| {r['top_score']} | {exp} | {retr} |"
        )
    lines += [
        "",
        "## Summary",
        "",
        "| Metric | v1 (baseline) | v2 (this run) | Target |",
        "|--------|--------------|---------------|--------|",
        f"| Hit-rate | 20.0% | {hit_rate}% | ≥ 80% |",
        f"| HITs | 2 | {hits} | 8+ |",
        f"| PARTIALs | 3 | {partials} | — |",
        f"| MISSes | 5 | {misses} | ≤ 2 |",
        f"| Pass / Fail | ❌ FAIL | {'✅ PASS' if hit_rate >= 80 else '❌ FAIL'} | — |",
        "",
        "## Changes from v1 → v2",
        "",
        "| Change | Reason |",
        "|--------|--------|",
        "| top-k 4 → 6 | More retrieval slots for multi-hop questions |",
        "| Fixed chunking → recursive | Preserves paragraph semantics; less mid-sentence splits |",
        f"| Chunk size 512 → {CHUNK_SIZE} chars | Smaller = more precise; less topic bleed |",
        f"| Per-doc cap added ({MAX_CHUNKS_PER_DOC} chunks) | Stops `conceptual-model.md` flooding every result |",
        "| Query expansion added | `Linear app support:` prefix improves MiniLM domain relevance |",
        "",
        "## Riskiest Assumption Status",
        "",
        "**Assumption:** MiniLM-L6-v2 + Chroma retrieves the correct doc in top-k for ≥ 80% of queries.",
        "",
        f"**Result:** {hit_rate}% — {'assumption holds ✅' if hit_rate >= 80 else 'assumption needs more tuning; see Week 16 experiments'}",
    ]
    FINDINGS_OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n[SAVE] FINDINGS.md written → {FINDINGS_OUT}")

    results_path = Path("spike/spike_results.json")
    with open(results_path, "w") as f:
        json.dump(rows, f, indent=2)
    print(f"[SAVE] Raw results → {results_path}")


def main():
    print("Northwind Support Copilot — De-Risk Spike v2")
    print(f"Fixes: recursive chunking | top-k={TOP_K} | per-doc cap={MAX_CHUNKS_PER_DOC} | query expansion\n")

    docs   = load_corpus(CORPUS_DIR)
    chunks = chunk_docs(docs)
    col, model = build_index(chunks)

    print(f"\n[EVAL] Running {len(GOLDEN_QUESTIONS)} questions...\n")
    rows = evaluate(col, model)
    hits, partials, misses, hit_rate = print_table(rows)
    save_findings(rows, hits, partials, misses, hit_rate)


if __name__ == "__main__":
    main()