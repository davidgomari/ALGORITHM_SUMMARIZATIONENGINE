import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

class HybridMerger:
    def __init__(self, alpha=0.6):
        self.alpha = alpha
        # Use a lightweight embedding model for semantic comparison
        # This is different from TF-IDF; it captures Meaning, not just keywords.
        self.encoder = SentenceTransformer('all-MiniLM-L6-v2') 

    def merge_scores(self, sentences, textrank_scores, oracle_summary):
        """
        Combines TextRank scores with Semantic Similarity to the Oracle Summary.
        
        Final_Score = (alpha * TextRank_Score) + ((1-alpha) * Semantic_Similarity)
        """
        
        # 1. Normalize TextRank scores (0 to 1)
        max_tr = max(textrank_scores.values()) if textrank_scores else 1
        norm_tr_scores = {k: v/max_tr for k,v in textrank_scores.items()}
        
        # 2. Compute Semantic Similarity (Oracle vs Original Sentences)
        # Encode sentences and the oracle summary
        sentence_embeddings = self.encoder.encode(sentences)
        oracle_embedding = self.encoder.encode([oracle_summary])
        
        # Calculate cosine similarity
        semantic_scores = cosine_similarity(sentence_embeddings, oracle_embedding).flatten()
        
        # 3. Calculate Hybrid Score
        final_scores = {}
        for i in range(len(sentences)):
            tr_score = norm_tr_scores.get(i, 0)
            sem_score = semantic_scores[i]
            
            # THE HYBRID FORMULA
            final_scores[i] = (self.alpha * tr_score) + ((1 - self.alpha) * sem_score)
            
        return final_scores

    def get_top_k(self, sentences, scores, k=3):
        """
        Selects top K sentences based on final scores and sorts them 
        by their original appearance order (to keep flow).
        """
        ranked_indices = sorted(scores, key=scores.get, reverse=True)[:k]
        ranked_indices.sort() # Sort by index to maintain text flow
        
        final_summary = [sentences[i] for i in ranked_indices]
        return " ".join(final_summary)