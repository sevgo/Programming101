#!/usr/bin/env python3

import unittest
from is_increasing import is_increasing


class Test_IS_Increasing(unittest.TestCase):

    def test_inc(self):
        self.assertTrue(is_increasing([3, 5, 8, 9, 22]))


if __name__ == "__main__":
    unittest.main()
