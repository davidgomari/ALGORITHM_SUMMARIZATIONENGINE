import nltk
import re

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

class TextPreprocessor:
    @staticmethod
    def clean_text(text):
        """
        Basic text cleaning: removes extra spaces, newlines.
        """
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    @staticmethod
    def split_sentences(text):
        """
        Splits text into a list of sentences using NLTK.
        """
        sentences = nltk.sent_tokenize(text)
        return [s for s in sentences if len(s.split()) > 3] # Filter very short sentences