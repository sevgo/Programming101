#!/usr/bin/env python3

import unittest
from sumOfDigits import sum_of_digits


class Test_Sum_Of_Digits(unittest.TestCase):

    def test_digits_s_sum(self):
        self.assertEqual(sum_of_digits(12345), 15)


if __name__ == "__main__":
    unittest.main()
