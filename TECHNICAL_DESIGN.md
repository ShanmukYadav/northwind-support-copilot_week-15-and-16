# Technical Design Document

# Northwind Support Copilot

## Architecture

```
User Query
     │
     ▼
Retriever
     │
     ▼
Sentence Transformer (all-MiniLM-L6-v2)
     │
     ▼
Chroma Vector Database
     │
     ▼
Top-K Retrieved Chunks
     │
     ▼
Prompt Builder
     │
     ▼
Groq Llama 3
     │
     ▼
Answer + Citations
```

---

## Components

### Data Ingestion

* Linear documentation scraped into Markdown.
* Total corpus: 17 documents.

### Chunking

* Recursive character chunking
* Chunk Size: 800
* Overlap: 150

### Embedding Model

* sentence-transformers/all-MiniLM-L6-v2
* Embedding Dimension: 384

### Vector Store

* ChromaDB
* Cosine similarity

### Retrieval

* Top-K = 6
* Query Expansion enabled
* Duplicate documents removed

### LLM

* Groq Llama 3

### Output

* Grounded answer
* Source document citations

---

## Pydantic Contracts

The project defines typed contracts for:

* RawDocument
* Chunk
* EmbeddedChunk
* RetrievalRequest
* RetrievalResponse
* PromptPayload
* LLMAnswer
* GoldenQuestion
* SpikeResult

---

## Bounded Action

Future versions may automatically draft customer support replies.

Current implementation focuses only on retrieval evaluation.

---

## Technologies

* Python
* ChromaDB
* Sentence Transformers
* Markdown
* Pydantic
* Groq API
