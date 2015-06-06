#!/usr/bin/env python3

import unittest
from zero_insert import zero_insert


class Test_zero_insert(unittest.TestCase):

    def test_zero_insert_type(self):
        self.assertIsInstance(zero_insert(116457), int)

    def test_zeroo_insert_result(self):
        self.assertTrue(6040406 == zero_insert(6446))


if __name__ == "__main__":
    unittest.main()
