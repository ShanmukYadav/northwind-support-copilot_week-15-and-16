# Risk Register

| Risk                               | Likelihood | Impact | Mitigation                              |
| ---------------------------------- | ---------- | ------ | --------------------------------------- |
| Incorrect retrieval                | High       | High   | Improve chunking and Top-K              |
| Hallucinated answers               | Medium     | High   | Restrict responses to retrieved context |
| Missing documentation              | Medium     | Medium | Update corpus regularly                 |
| Large documents dominate retrieval | Medium     | Medium | Limit maximum chunks per document       |
| Embedding quality                  | Medium     | High   | Evaluate different embedding models     |

---

## Riskiest Assumption

The retrieval system can retrieve the correct document for most support questions.

---

## De-risk Spike

A retrieval spike was implemented using:

* Sentence Transformers
* ChromaDB
* Recursive Chunking

Result:

**Retrieval Hit Rate = 80%**

The spike demonstrates that semantic retrieval is feasible for the selected corpus.
# Risk Register

| Risk                               | Likelihood | Impact | Mitigation                              |
| ---------------------------------- | ---------- | ------ | --------------------------------------- |
| Incorrect retrieval                | High       | High   | Improve chunking and Top-K              |
| Hallucinated answers               | Medium     | High   | Restrict responses to retrieved context |
| Missing documentation              | Medium     | Medium | Update corpus regularly                 |
| Large documents dominate retrieval | Medium     | Medium | Limit maximum chunks per document       |
| Embedding quality                  | Medium     | High   | Evaluate different embedding models     |

---

## Riskiest Assumption

The retrieval system can retrieve the correct document for most support questions.

---

## De-risk Spike

A retrieval spike was implemented using:

* Sentence Transformers
* ChromaDB
* Recursive Chunking

Result:

**Retrieval Hit Rate = 80%**

The spike demonstrates that semantic retrieval is feasible for the selected corpus.
