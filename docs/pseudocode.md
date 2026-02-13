Algorithm: Hybrid_TextRank_Summarizer
Input: Text T, Parameter top_k, Parameter alpha
Output: Summary S_final

1. Sentences S = Split_Into_Sentences(T)
2. N = Length(S)
3. SimilarityMatrix M = ZeroMatrix(N, N)

// Phase 1: Classical Graph Construction
4. For i from 0 to N-1:
5.    For j from 0 to N-1:
6.        If i != j:
7.            M[i][j] = Compute_Cosine_Similarity(S[i], S[j])

// Phase 2: Graph Ranking (PageRank)
8. Scores = Initialize_Scores(1/N)
9. Repeat until convergence:
10.    NewScores = (1-d) + d * (M_transposed * Scores)
11.    Scores = NewScores

// Phase 3: LLM Oracle Integration
12. LLM_Summary = Call_LLM_API("Summarize strictly in 2 sentences:", T)
13. HybridScores = Array(N)

14. For i from 0 to N-1:
15.    Sim_with_Oracle = Compute_Semantic_Similarity(S[i], LLM_Summary)
16.    HybridScores[i] = (alpha * Scores[i]) + ((1-alpha) * Sim_with_Oracle)

// Phase 4: Selection
17. RankedIndices = Sort_Descending(HybridScores)
18. SelectedIndices = RankedIndices[0 : top_k]
19. Sort SelectedIndices to maintain original text order
20. Return Concatenate(S[i] for i in SelectedIndices)