class Config:
    """
    Configuration for the Hybrid Summarization Engine.
    """
    # TextRank Parameters
    TOP_K_SENTENCES = 3  # Number of sentences to extract
    DAMPING_FACTOR = 0.85 # PageRank damping factor
    SIMILARITY_THRESHOLD = 0.3 # Minimum similarity to create an edge in graph

    # LLM Parameters
    # Using 'flan-t5-base' because it is small, fast, and works well on Kaggle CPU/GPU
    LLM_MODEL_NAME = "google/flan-t5-base" 
    MAX_LLM_LENGTH = 150
    MIN_LLM_LENGTH = 40

    # Merger (Hybrid) Parameters
    # ALPHA controls the trade-off:
    # 1.0 = Pure TextRank
    # 0.0 = Pure Semantic Similarity to LLM
    # 0.6 = Balanced approach (60% Graph Centrality, 40% LLM Alignment)
    ALPHA = 0.6