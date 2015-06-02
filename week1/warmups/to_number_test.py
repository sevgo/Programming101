#!/usr/bin/env python3


import unittest
from to_number import to_number


class Test_to_Number(unittest.TestCase):

    def test_to_number_type(self):
        self.assertIsInstance(to_number([1, 3, 5, 7]), int)

    def test_the_number(self):
        self.assertEqual(to_number([6, 6, 6]), 666)


if __name__ == "__main__":
    unittest.main()
