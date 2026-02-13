import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from src.main import run_project
from src.text_rank import TextRankSummarizer
from src.preprocessor import TextPreprocessor
from tests.test_data import TEST_CASES

class TestSummarizationEngine(unittest.TestCase):
    
    def setUp(self):
        self.processor = TextPreprocessor()
        self.ranker = TextRankSummarizer()

    def test_preprocessing(self):
        """Test if sentences are split correctly"""
        text = "Hello world. This is a test."
        sents = self.processor.split_sentences(text)
        self.assertEqual(len(sents), 2)

    def test_failure_case(self):
        """Test how system handles too short text"""
        failure_text = TEST_CASES[-1]['text'] # The "Hello." case
        sents = self.processor.split_sentences(failure_text)
        self.assertTrue(len(sents) <= 1) 

    def test_pipeline_execution(self):
        """Run all test cases and ensure no crashes"""
        print("\nRunning Bulk Tests...")
        for case in TEST_CASES:
            print(f"Testing Case {case['id']} ({case['type']})...", end=" ")
            try:
                sents = self.processor.split_sentences(case['text'])
                if len(sents) > 1:
                    scores = self.ranker.rank_sentences(sents)
                    self.assertIsNotNone(scores)
                print("OK")
            except Exception as e:
                self.fail(f"Crashed on case {case['id']}: {e}")

if __name__ == '__main__':
    unittest.main()