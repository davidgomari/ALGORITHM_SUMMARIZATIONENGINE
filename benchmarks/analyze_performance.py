import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt

# 1. Get the directory where THIS script is located (tests/)
current_dir = os.path.dirname(os.path.abspath(__file__))
# 2. Get the parent directory (project root)
project_root = os.path.dirname(current_dir)
# 3. Get the src directory
src_path = os.path.join(project_root, 'src')

# 4. Add 'src' to system path so we can import 'main', 'config', etc. directly
sys.path.append(src_path)

from text_rank import TextRankSummarizer
from preprocessor import TextPreprocessor

def generate_dummy_text(n_sentences):
    """Generates a dummy text with N sentences."""
    sentence = "This is a sample sentence for performance testing algorithm complexity. "
    return sentence * n_sentences

def run_benchmark():
    input_sizes = [10, 50, 100, 200, 300, 500]
    times = []

    print("Starting Performance Analysis...")
    ranker = TextRankSummarizer()
    
    for n in input_sizes:
        text = generate_dummy_text(n)
        sentences = TextPreprocessor.split_sentences(text)
        
        start_time = time.time()
        ranker.rank_sentences(sentences)
        end_time = time.time()
        
        duration = end_time - start_time
        times.append(duration)
        print(f"N={n}, Time={duration:.4f}s")

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, times, marker='o', label='Actual Time')
    
    # Theoretical O(N^2) curve for comparison
    theoretical = [x**2 for x in input_sizes]
    scale_factor = times[-1] / theoretical[-1] 
    theoretical = [t * scale_factor for t in theoretical]
    
    plt.plot(input_sizes, theoretical, '--', label='Theoretical O(N^2)')
    
    plt.title('Algorithm Performance Analysis (Time Complexity)')
    plt.xlabel('Number of Sentences (N)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('benchmarks/performance_plot.png')
    print("Plot saved to benchmarks/performance_plot.png")

if __name__ == "__main__":
    run_benchmark()