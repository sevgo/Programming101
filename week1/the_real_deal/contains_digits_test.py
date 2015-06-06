#!/usr/bin/env python3

import unittest
from contains_digits import contains_digits


class Test_Digits_Containning(unittest.TestCase):

    def test_containning_digits(self):
        self.assertTrue(contains_digits(297876954274, [2, 7, 5, 9]))


if __name__ == "__main__":
    unittest.main()
