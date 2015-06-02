import unittest
from to_digits import to_digits


class Test_to_Digits(unittest.TestCase):

    def test_to_digits_type(self):
        self.assertIsInstance(to_digits(12345), list)

    def test_to_digit_len(self):
        self.assertEqual(len(to_digits(9999)), 4)

    def test_to_digit_random_digit(self):
        self.assertEqual(to_digits(22022)[2], 0)


if __name__ == "__main__":
    unittest.main()
