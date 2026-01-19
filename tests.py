# tests.py
import unittest
from main import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15, "Fail")
        self.assertEqual(add(-1, 1), 0, "Fail")
        print("✅ Addition Tests Passed")

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5, "Fail")
        self.assertEqual(subtract(10, -5), 15, "Fail")
        print("✅ Subtraction Tests Passed")

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12, "Fail")
        print("✅ Multiplication Tests Passed")

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5, "Fail")
        self.assertIsNone(divide(5, 0), "Fail")
        print("✅ Division Tests Passed")

if __name__ == '__main__':
    print("--- 🤖 RUNNING AUTO-GRADER 🤖 ---")
    unittest.main(exit=False)