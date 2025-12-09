# mcq_evaluator/evaluator.py

import csv
import os
from pathlib import Path
from typing import Dict, List, Tuple

class MCQEvaluator:
    def __init__(self, csv_path: str):
        self.csv_path = Path(csv_path)
        self.results = []
        
    def load_quiz_data(self) -> List[Dict]:
        """Loads quiz data from CSV."""
        if not self.csv_path.exists():
            raise FileNotFoundError(f"CSV file not found: {self.csv_path}")
            
        with open(self.csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    
    def evaluate_answers(self) -> Tuple[int, int, float, List[Dict]]:
        """
        Returns: (correct_count, total_questions, percentage_score, detailed_results)
        """
        quiz_data = self.load_quiz_data()
        correct_count = 0
        
        for row in quiz_data:
            is_correct = row['correct_answer'].strip().lower() == row['user_answer'].strip().lower()
            if is_correct:
                correct_count += 1
                
            self.results.append({
                'question': row['question'],
                'correct_answer': row['correct_answer'],
                'user_answer': row['user_answer'],
                'is_correct': is_correct
            })
        
        total = len(quiz_data)
        percentage = (correct_count / total * 100) if total > 0 else 0
        
        return correct_count, total, percentage, self.results
    
    def print_detailed_report(self):
        """Prints a formatted report."""
        correct, total, percentage, results = self.evaluate_answers()
        
        print(f"\n📊 MCQ Evaluation Report")
        print("="*50)
        print(f"Total Questions: {total}")
        print(f"Correct Answers: {correct}")
        print(f"Incorrect Answers: {total - correct}")
        print(f"Score: {percentage:.2f}%\n")
        
        print("Detailed Results:")
        print("-" * 50)
        for i, result in enumerate(results, 1):
            status = "✅" if result['is_correct'] else "❌"
            print(f"{i}. {status} {result['question']}")
            print(f"   Your Answer: '{result['user_answer']}' | Correct: '{result['correct_answer']}'\n")

def evaluate_quiz(csv_path: str):
    """Convenience function to run evaluation."""
    evaluator = MCQEvaluator(csv_path)
    evaluator.print_detailed_report()

if __name__ == "__main__":
    # Default usage
    sample_csv = Path(__file__).parent / "sample_quiz.csv"
    evaluate_quiz(sample_csv)