import unittest
from math_quiz import add, subtract, multiply, divide, generate_quiz_question

class TestMathQuiz(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 7), 3)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 4), -8)


    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(8, 2), 4)
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_generate_quiz_question(self):
        question, answer = generate_quiz_question()
        self.assertTrue(isinstance(question, str))
        self.assertTrue(isinstance(answer, (int, float)))

if __name__ == '__main__':
    unittest.main()
