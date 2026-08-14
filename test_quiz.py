import unittest
from start_quiz_screen import user_answer
def calculate_precent(score,total_questions):
    if total_questions == 0:
        return 0
    else:
        return (score/total_questions)*100

class Test_quiz(unittest.TestCase):
    def test_user_answer(self):
        self.assertTrue(user_answer("a","A"))
        self.assertTrue(user_answer(" B ","B"))
        self.assertTrue(user_answer("c","C"))
        self.assertFalse("A","B")

    def test_score_and_precent(self):
        total_questions = 5
        correct_answer = 4
        precent = calculate_precent(correct_answer,total_questions)
        self.assertEqual(precent,80.0)
        self.assertEqual(calculate_precent(0,5),0.0)
        self.assertEqual(calculate_precent(5,5),100.0)

unittest.main()