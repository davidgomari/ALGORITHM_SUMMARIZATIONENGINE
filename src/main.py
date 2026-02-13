from config import Config
from preprocessor import TextPreprocessor
from textrank import TextRankSummarizer
from llm_engine import LLMSummarizer
from merger import HybridMerger
import time

def run_project(input_text):
    print("--- Phase 1: Algorithm Initialization ---")
    
    # 1. Preprocessing
    sentences = TextPreprocessor.split_sentences(input_text)
    print(f"Input Text: {len(sentences)} sentences.")
    
    # 2. Classical Algorithm (TextRank)
    print("\n--- Running TextRank (Graph-based) ---")
    start_time = time.time()
    tr_engine = TextRankSummarizer()
    tr_scores = tr_engine.rank_sentences(sentences)
    print(f"TextRank completed in {time.time() - start_time:.4f}s")
    
    # 3. LLM Oracle (Abstractive)
    print("\n--- Running LLM (Oracle Component) ---")
    llm_engine = LLMSummarizer(Config.LLM_MODEL_NAME)
    oracle_summary = llm_engine.generate_oracle_summary(input_text)
    print(f"Oracle Summary: {oracle_summary}")
    
    # 4. Hybrid Merger
    print("\n--- Running Hybrid Merger ---")
    merger = HybridMerger(alpha=Config.ALPHA)
    
    # Calculate combined scores
    final_scores = merger.merge_scores(sentences, tr_scores, oracle_summary)
    
    # Generate Final Summary
    final_summary = merger.get_top_k(sentences, final_scores, k=Config.TOP_K_SENTENCES)
    
    print("\n" + "="*40)
    print("FINAL HYBRID SUMMARY")
    print("="*40)
    print(final_summary)
    print("="*40)

if __name__ == "__main__":
    # Sample Input (A tech article snippet)
    sample_text = """
    Deep learning is part of a broader family of machine learning methods based on artificial neural networks with representation learning.
    Learning can be supervised, semi-supervised or unsupervised. 
    Deep-learning architectures such as deep neural networks, deep belief networks, deep reinforcement learning, recurrent neural networks and convolutional neural networks have been applied to fields including computer vision, speech recognition, natural language processing, machine translation, bioinformatics, drug design, medical image analysis, material inspection and board game programs, where they have produced results comparable to and in some cases surpassing human expert performance.
    Artificial neural networks (ANNs) were inspired by information processing and distributed communication nodes in biological systems. 
    ANNs have various differences from biological brains. 
    Specifically, artificial neural networks tend to be static and symbolic, while the biological brain of most living organisms is dynamic (plastic) and analog.
    """
    
    run_project(sample_text)