import unittest
from fibonacci import fibonacci


class Test_Fibonacci(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(len(fibonacci(10)), 10)



if __name__ == "__main__":
    unittest.main()
