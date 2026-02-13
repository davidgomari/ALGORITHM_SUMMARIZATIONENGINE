import numpy as np
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TextRankSummarizer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')

    def build_similarity_matrix(self, sentences):
        """
        Constructs a similarity matrix based on Cosine Similarity of TF-IDF vectors.
        Time Complexity: O(N^2 * D) where N=sentences, D=vocab size.
        """
        
        # OPTIMIZATION: Truncate large inputs to optimize performance
        MAX_SENTENCES = 500
        if len(sentences) > MAX_SENTENCES:
            print(f"Warning: Input too long ({len(sentences)}). Truncating to {MAX_SENTENCES} for performance.")
            sentences = sentences[:MAX_SENTENCES]
        
        tfidf_matrix = self.vectorizer.fit_transform(sentences)
        similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
        return similarity_matrix

    def rank_sentences(self, sentences, damping=0.85):
        """
        Applies PageRank algorithm to the similarity graph.
        Returns a dictionary: {sentence_index: score}
        """
        if not sentences:
            return {}

        # 1. Build the similarity matrix
        sim_matrix = self.build_similarity_matrix(sentences)
        
        # 2. Convert matrix to a Graph
        nx_graph = nx.from_numpy_array(sim_matrix)
        
        # 3. Apply PageRank
        # This solves the equation: PR(u) = (1-d) + d * Sum(PR(v) / OutDegree(v))
        try:
            scores = nx.pagerank(nx_graph, alpha=damping, max_iter=100)
        except nx.PowerIterationFailedConvergence:
            # Fallback if graph doesn't converge
            scores = {i: 1.0/len(sentences) for i in range(len(sentences))}
            
        return scores