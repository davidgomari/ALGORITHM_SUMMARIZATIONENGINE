# Algorithmic Summarization Engine (Group 7)

## Project Description
This project implements a hybrid summarization engine combining classical Graph-based algorithms (TextRank) with Large Language Models (LLMs) to produce high-quality extractive summaries.

## Algorithm Path: Path 3 (Hybrid)
1. **Classical:** TextRank with TF-IDF/Cosine Similarity.
2. **LLM Role:** Oracle-based evaluation and re-ranking.
3. **Merger:** Weighted linear combination of graph centrality and semantic alignment with the oracle.

## Structure
- `src/`: Source code (Python).
- `docs/`: Complexity analysis and algorithmic design documents.
- `tests/`: Unit tests and sample inputs.

## Complexity
- **Time:** O(N^2) due to graph construction.
- **Space:** O(N^2) for adjacency matrix storage.