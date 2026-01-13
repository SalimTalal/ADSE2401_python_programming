# Python file/script to demonstrate unit testing the factorial() function

# Import the required modules
import unittest
from .factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_positive_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_negative_factorial(self):
        with self.assertRaises(ValueError) as ve:
            factorial(-7)
        self.assertEqual(str(ve.exception), "Factorial of negative numbers is not defined!")

# Run the test
if __name__ == '__main__':
    unittest.main()