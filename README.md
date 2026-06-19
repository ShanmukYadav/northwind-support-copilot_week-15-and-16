# Northwind Support Copilot

## Overview

Northwind Support Copilot is an AI-powered Retrieval-Augmented Generation (RAG) system designed to assist customer support agents by retrieving relevant product documentation and generating grounded responses with citations.

The project demonstrates a complete retrieval pipeline using semantic search with ChromaDB and Sentence Transformers. The primary objective is to reduce support response time while improving answer consistency and reliability.

This project was developed as part of the Futurense AI Clinic Week 15 Mini Project: **Spec & De-risk**.

---

# Problem Statement

Support teams often spend significant time searching through scattered documentation to answer customer queries.

Challenges include:

* Long response times
* Inconsistent answers
* Difficult onboarding of new support agents
* Large documentation corpus

The goal is to build an AI assistant capable of retrieving the correct documentation and producing grounded responses.

---

# Features

* Documentation scraping
* Markdown corpus creation
* Recursive document chunking
* Sentence embeddings using MiniLM
* ChromaDB vector database
* Semantic similarity search
* Query expansion
* Retrieval evaluation using Golden Questions
* Retrieval hit-rate analysis
* Typed data contracts using Pydantic

---

# Tech Stack

* Python 3.11+
* Sentence Transformers
* ChromaDB
* Pydantic
* BeautifulSoup
* Markdownify
* Requests

---

# Project Architecture

```text
                User Question
                      │
                      ▼
              Query Expansion
                      │
                      ▼
         Sentence Transformer
                      │
                      ▼
              Chroma Vector DB
                      │
                      ▼
            Top-K Retrieval
                      │
                      ▼
          Retrieved Documents
                      │
                      ▼
          (Future) Groq LLM
                      │
                      ▼
        Answer with Citations
```

---

# Repository Structure

```text
Northwind-Support-Copilot/
│
├── corpus/
│   ├── conceptual-model.md
│   ├── configuring-workflows.md
│   ├── display-options.md
│   ├── filters.md
│   ├── github.md
│   ├── import-issues.md
│   ├── issue-relations.md
│   ├── labels.md
│   ├── notifications.md
│   ├── parent-and-sub-issues.md
│   ├── project-documents.md
│   ├── project-overview.md
│   ├── projects.md
│   ├── select-issues.md
│   ├── start-guide.md
│   ├── teams.md
│   └── triage.md
│
├── design/
│   └── contracts.py
│
├── spike/
│   ├── spike_retrieval.py
│   └── spike_results.json
│
├── PRD.md
├── TECHNICAL_DESIGN.md
├── RISK_REGISTER.md
├── FINDINGS.md
├── README.md
└── requirements.txt
```

---

# Retrieval Pipeline

1. Load markdown documents
2. Perform recursive chunking
3. Generate MiniLM embeddings
4. Store vectors in ChromaDB
5. Expand user query
6. Retrieve Top-K relevant chunks
7. Evaluate retrieval performance

---

# Embedding Model

Model:

```
sentence-transformers/all-MiniLM-L6-v2
```

Embedding Dimension:

```
384
```

Similarity Metric:

```
Cosine Similarity
```

---

# Chunking Strategy

| Parameter       | Value                        |
| --------------- | ---------------------------- |
| Strategy        | Recursive Character Chunking |
| Chunk Size      | 800                          |
| Chunk Overlap   | 150                          |
| Top-K Retrieval | 6                            |

---

# Retrieval Evaluation

A golden evaluation dataset consisting of 10 manually curated questions was created.

Question Categories:

* Easy
* Multi-Hop
* Adversarial

Evaluation measures whether the expected document appears within the Top-K retrieved results.

---

# Results

| Metric             |   Value |
| ------------------ | ------: |
| Questions          |      10 |
| HIT                |       8 |
| PARTIAL            |       1 |
| MISS               |       1 |
| Retrieval Hit Rate | **80%** |

---

# Findings

The retrieval spike demonstrates that semantic retrieval using ChromaDB and Sentence Transformers is effective for documentation search.

Observations:

* Recursive chunking improved retrieval quality.
* Query expansion improved semantic matching.
* Limiting maximum chunks per document reduced retrieval bias.
* The retrieval pipeline achieved an overall hit rate of **80%**, validating the project's primary assumption.

---

# Future Improvements

* Hybrid Retrieval (BM25 + Vector Search)
* Cross-Encoder Re-ranking
* Larger Golden Evaluation Set
* LLM-based Answer Generation
* Source Citation Validation
* Langfuse Observability
* Ragas Evaluation Metrics
* DeepEval Testing

---

# How to Run

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run Retrieval Spike

```bash
python spike/spike_retrieval.py
```

---

## Expected Output

```text
HIT: 8
PARTIAL: 1
MISS: 1

Retrieval Hit Rate: 80%
```

---

# Key Deliverables

* Product Requirements Document (PRD)
* Technical Design Document
* Risk Register
* Pydantic Data Contracts
* Retrieval Spike
* Findings Report
* Markdown Documentation Corpus

---

# Author

**Kukati Shanmuk**

Futurense AI Clinic

Week 15 – Spec & De-risk

Northwind Support Copilot
