#!/usr/bin/env python3

import unittest
from fib_number import fib_number


class Test_Fib_Number(unittest.TestCase):

    def test_is_number_fib_number(self):
        self.assertIsInstance(fib_number(3), int)


    def test_fib_number(self):
        self.assertEqual(fib_number(10), 11235813213455)


if __name__ == "__main__":
    unittest.main()
