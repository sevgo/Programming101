import unittest
from factorial import factorial


class Test_Factorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(1), 1)

if __name__ == "__main__":
    unittest.main()
