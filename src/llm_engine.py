from transformers import pipeline
import torch

class LLMSummarizer:
    def __init__(self, model_name):
        self.model_name = model_name
        # Check if GPU is available
        self.device = 0 if torch.cuda.is_available() else -1
        print(f"Loading LLM: {model_name} on device {'GPU' if self.device==0 else 'CPU'}...")
        
        self.summarizer = pipeline(
            "summarization", 
            model=model_name, 
            device=self.device
        )

    def generate_oracle_summary(self, text, max_len=150, min_len=40):
        """
        Generates an abstractive summary.
        This summary acts as the 'Ground Truth' or 'Oracle' for the merger.
        """
        try:
            # Chunking text if it's too long (simplified for this demo)
            summary = self.summarizer(
                text[:2000], # Limit input to avoid OOM on Kaggle
                max_length=max_len, 
                min_length=min_len, 
                do_sample=False
            )
            return summary[0]['summary_text']
        except Exception as e:
            print(f"Error in LLM generation: {e}")
            return ""