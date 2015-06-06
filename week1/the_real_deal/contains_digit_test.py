#!/usr/bin/env python3

import unittest
from contains_digit import contains_digit


class Test_Contains_Digit(unittest.TestCase):

    def test_digit(self):
        self.assertTrue(contains_digit(142059, 0))


if __name__ == "__main__":
    unittest.main()
