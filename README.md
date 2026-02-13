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

## Testing Strategy
We implemented a robust testing suite in `tests/` covering:
- **Easy/Medium/Hard Inputs:** Verified algorithm stability across different text complexities.
- **Edge Cases:** Handled empty strings and single-sentence inputs gracefully.
- **Automated Tests:** Run `python tests/run_tests.py` to validate.

## Performance Analysis
Empirical analysis confirms the **O(N^2)** theoretical complexity derived in Phase 1.
- Benchmarks run on inputs from N=10 to N=500.
- **Optimization:** Introduced a truncation heuristic for N > 500 to prevent performance degradation on CPU.

## How to Run the Demo
Open the Jupyter Notebook:
```bash
jupyter notebook demo.ipynb
```