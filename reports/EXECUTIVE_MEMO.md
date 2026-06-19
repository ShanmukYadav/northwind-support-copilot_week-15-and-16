# Executive Memo

## Project

Northwind Support Copilot

## Objective

Develop a Retrieval-Augmented Generation (RAG) support assistant capable of
answering questions using Linear documentation.

## Architecture

- Markdown corpus
- Recursive chunking
- SentenceTransformer embeddings
- ChromaDB vector store
- Groq Llama model
- Prompt engineering
- Retrieval-Augmented Generation pipeline

## Achievements

- Successfully indexed the documentation corpus.
- Built an end-to-end RAG pipeline.
- Achieved an 80% retrieval hit rate during the retrieval spike.
- Implemented retrieval, prompt assembly, and answer generation.
- Created a 40-question golden evaluation dataset.
- Added observability hooks for Langfuse.
- Conducted a retrieval Top-K experiment.

## Challenges

- Retrieval quality varied for workflow-related queries because of the structure
  of the source documentation.
- Python 3.14 compatibility issues required migrating to Python 3.11 for
  evaluation tooling.

## Future Work

- Complete automated Ragas evaluation using reference answers.
- Improve document preprocessing.
- Add reranking for improved retrieval quality.
- Deploy the assistant as a web application.