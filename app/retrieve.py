import time
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

from app.config import (
    CHROMA_DIR,
    COLLECTION,
    EMBED_MODEL,
    TOP_K,
)
from app.ingest import load_documents, chunk_documents


def build_index():
    """
    Loads and chunks documents via the ingest module, then embeds and indexes 
    them in ChromaDB. Returns the collection and embedding model.
    """
    print(f"[EMBED] Loading {EMBED_MODEL} ...")
    model = SentenceTransformer(EMBED_MODEL)
    
    # Ensure Chroma directory exists
    chroma_path = Path(CHROMA_DIR)
    chroma_path.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(chroma_path))

    # Fetch and chunk corpus via the ingestion module
    docs = load_documents()
    chunks = chunk_documents(docs)

    # Check for existing cache
    existing = [c.name for c in client.list_collections()]
    if COLLECTION in existing:
        col = client.get_collection(COLLECTION)
        if col.count() == len(chunks):
            print(f"[EMBED] Cache hit ({col.count()} chunks)")
            return col, model
        # Rebuild if the chunk count doesn't match
        client.delete_collection(COLLECTION)

    col = client.create_collection(COLLECTION, metadata={"hnsw:space": "cosine"})
    print(f"[EMBED] Indexing {len(chunks)} chunks...")
    t0 = time.time()

    BATCH = 64
    all_embeddings = []
    texts     = [c["text"]     for c in chunks]
    ids       = [c["chunk_id"] for c in chunks]
    metadatas = [{"doc_id": c["doc_id"], "title": c["title"]} for c in chunks]

    # Batch encode to avoid memory overflow
    for i in range(0, len(texts), BATCH):
        embs = model.encode(texts[i:i+BATCH], show_progress_bar=False).tolist()
        all_embeddings.extend(embs)

    col.upsert(ids=ids, embeddings=all_embeddings, documents=texts, metadatas=metadatas)
    print(f"[EMBED] Done in {time.time()-t0:.1f}s")
    
    return col, model


def retrieve(query: str, col, model) -> list[dict]:
    """
    Retrieves the top-k chunks for a given query using the existing model and collection.
    """
    # Query expansion: documentation prefix improves MiniLM relevance for short queries
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


if __name__ == "__main__":
    collection, model = build_index()

    print()

    results = retrieve(
        "How do I configure workflows?",
        collection,
        model
    )

    print(f"Retrieved {len(results)} chunks\n")

    for r in results:
        print(f"{r['doc_id']:<30} score={r['score']}")