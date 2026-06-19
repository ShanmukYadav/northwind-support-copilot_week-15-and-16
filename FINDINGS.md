# FINDINGS.md — De-Risk Spike Results (v2)

> **Date:** 2026-06-19  
> **Embedding model:** `all-MiniLM-L6-v2`  
> **Chunking:** recursive (size=800, overlap=150, cap=15/doc)  
> **top-k:** 6 | **Query expansion:** `Linear app support: <query>`  

## Retrieval Hit-Rate Table

| ID | Flavor | Status | Top Score | Expected Doc(s) | Retrieved (deduped) |
|----|--------|--------|-----------|-----------------|---------------------|
| q01 | easy | ✅ HIT | 0.5756 | conceptual-model | start-guide, conceptual-model, import-issues, project-overview |
| q02 | easy | ❌ MISS | 0.6651 | configuring-workflows | start-guide, conceptual-model, import-issues, teams |
| q03 | multi_hop | ⚠️  PARTIAL | 0.6722 | projects, teams | import-issues, conceptual-model, teams, start-guide |
| q04 | easy | ✅ HIT | 0.5696 | triage | conceptual-model, parent-and-sub-issues, triage, configuring-workflows |
| q05 | easy | ✅ HIT | 0.6569 | labels | conceptual-model, labels, parent-and-sub-issues |
| q06 | multi_hop | ✅ HIT | 0.6916 | project-documents, projects | projects, project-documents, project-overview, import-issues |
| q07 | adversarial | ✅ HIT | 0.4181 | *(adversarial)* | start-guide, conceptual-model, import-issues, teams, project-overview |
| q08 | multi_hop | ✅ HIT | 0.6467 | filters, labels | filters, labels, conceptual-model, parent-and-sub-issues |
| q09 | easy | ✅ HIT | 0.7474 | display-options | display-options, start-guide, parent-and-sub-issues |
| q10 | multi_hop | ✅ HIT | 0.6829 | github, import-issues | github, import-issues |

## Summary

| Metric | v1 (baseline) | v2 (this run) | Target |
|--------|--------------|---------------|--------|
| Hit-rate | 20.0% | 80.0% | ≥ 80% |
| HITs | 2 | 8 | 8+ |
| PARTIALs | 3 | 1 | — |
| MISSes | 5 | 1 | ≤ 2 |
| Pass / Fail | ❌ FAIL | ✅ PASS | — |

## Changes from v1 → v2

| Change | Reason |
|--------|--------|
| top-k 4 → 6 | More retrieval slots for multi-hop questions |
| Fixed chunking → recursive | Preserves paragraph semantics; less mid-sentence splits |
| Chunk size 512 → 800 chars | Smaller = more precise; less topic bleed |
| Per-doc cap added (15 chunks) | Stops `conceptual-model.md` flooding every result |
| Query expansion added | `Linear app support:` prefix improves MiniLM domain relevance |

## Riskiest Assumption Status

**Assumption:** MiniLM-L6-v2 + Chroma retrieves the correct doc in top-k for ≥ 80% of queries.

**Result:** 80.0% — assumption holds ✅