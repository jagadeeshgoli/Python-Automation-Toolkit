# tests/test_mcq_evaluator.py

import unittest
import tempfile
from pathlib import Path
from mcq_evaluator.evaluator import MCQEvaluator

class TestMCQEvaluator(unittest.TestCase):
    def setUp(self):
        """Create a temporary CSV for testing."""
        self.test_csv = Path(tempfile.mktemp(suffix=".csv"))
        sample_data = """question,correct_answer,user_answer
"What is 2+2?",4,4
"Capital of India?","New Delhi","New Delhi"
"Python is a...","Programming Language","Scripting Language"
"What does len('abc') return?",3,2
"""
        self.test_csv.write_text(sample_data)
    
    def tearDown(self):
        """Clean up test CSV."""
        if self.test_csv.exists():
            self.test_csv.unlink()
    
    def test_evaluate_answers(self):
        """Test scoring logic."""
        evaluator = MCQEvaluator(self.test_csv)
        correct, total, percentage, results = evaluator.evaluate_answers()
        
        self.assertEqual(total, 4)
        self.assertEqual(correct, 2)  # 2+2 and len('abc') were wrong in sample
        self.assertEqual(percentage, 50.0)
    
    def test_case_insensitive_comparison(self):
        """Test that answers are case-insensitive."""
        # Create test CSV with different cases
        test_csv = Path(tempfile.mktemp(suffix=".csv"))
        case_data = """question,correct_answer,user_answer
"Test?","YES","yes
"""
        test_csv.write_text(case_data)
        
        evaluator = MCQEvaluator(test_csv)
        correct, total, _, _ = evaluator.evaluate_answers()
        
        self.assertEqual(correct, 1)
        test_csv.unlink()  # Clean up

if __name__ == "__main__":
    unittest.main()