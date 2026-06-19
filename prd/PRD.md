# Product Requirements Document (PRD)

# Northwind Support Copilot

## 1. Problem Statement

Northwind is a mid-sized B2B SaaS company whose support agents spend significant time searching through scattered documentation to answer customer questions. This increases response time, causes inconsistent answers, and makes onboarding new support agents difficult.

The goal of the Northwind Support Copilot is to provide an AI-powered assistant that retrieves relevant documentation, generates grounded responses with citations, and reduces the time required to answer support queries.

---

# 2. Users

### Primary User

* Customer Support Agents

### Secondary Users

* Support Managers
* New Support Team Members

---

# 3. User Stories

### Story 1

As a support agent, I want to ask questions in natural language so I can quickly find the correct documentation.

### Story 2

As a support manager, I want consistent answers so that customers receive reliable information.

### Story 3

As a new employee, I want an assistant that explains documentation with references so I can learn the product faster.

---

# 4. Scope

## Included

* Document ingestion
* Markdown corpus
* Chunking
* Sentence embeddings
* Chroma vector database
* Semantic retrieval
* LLM answer generation
* Source citations

## Not Included

* User authentication
* Ticket creation
* CRM integration
* Voice interface
* Fine-tuned models

---

# 5. Functional Requirements

* Load documentation corpus
* Split documents into chunks
* Generate embeddings
* Store embeddings in Chroma
* Retrieve top-k relevant chunks
* Generate answers using Groq Llama
* Display source citations
* Return "I don't know" when the answer is unavailable

---

# 6. Non-Functional Requirements

| Requirement        | Target      |
| ------------------ | ----------- |
| Retrieval latency  | < 2 seconds |
| Cost per query     | < $0.01     |
| Availability       | 95%         |
| Retrieval hit rate | ≥80%        |
| Grounded responses | Required    |

---

# 7. Success Metrics (KPIs)

| KPI                    | Target | Do Not Ship |
| ---------------------- | ------ | ----------- |
| Retrieval Hit Rate     | ≥80%   | <60%        |
| Faithfulness           | ≥90%   | <70%        |
| Answer Relevancy       | ≥80%   | <60%        |
| Context Recall         | ≥80%   | <60%        |
| Response Latency       | <2 sec | >5 sec      |
| Support Time Reduction | 30%    | <10%        |

---

# 8. Risks

| Risk                               | Mitigation                                 |
| ---------------------------------- | ------------------------------------------ |
| Retrieval returns wrong document   | Improve chunking and Top-K                 |
| Hallucinated answers               | Restrict answers to retrieved context      |
| Poor embeddings                    | Experiment with different embedding models |
| Large documents dominate retrieval | Limit chunks per document                  |
| Missing documentation              | Regular corpus updates                     |

---

# 9. MVP Deliverables

* Working document ingestion
* Chroma vector database
* Retrieval pipeline
* LLM-based question answering
* Source citations
* Evaluation using 10 golden questions
* Retrieval hit-rate report

---

# 10. Current Results

The retrieval spike was evaluated using ten manually created golden questions.

Results:

* Hit: 8
* Partial: 1
* Miss: 1

Final Retrieval Hit Rate:

**80%**

The project successfully demonstrates that semantic retrieval using Sentence Transformers and Chroma can retrieve the correct documentation for the majority of support queries.
