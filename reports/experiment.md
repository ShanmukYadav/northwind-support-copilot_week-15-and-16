# Retrieval Experiment

## Objective

Evaluate the effect of retrieval Top-K on answer quality.

## Configuration A

Top-K = 4

## Configuration B

Top-K = 6

## Observation

Increasing Top-K provided more context but occasionally introduced unrelated
documents. Top-K = 4 produced more focused answers while Top-K = 6 improved
coverage for multi-document questions.

## Conclusion

Top-K = 4 was selected as the default retrieval configuration because it
provided the best balance between relevance and context size.git add reports/experiment.md
