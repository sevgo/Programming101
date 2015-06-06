#!/usr/bin/env python3

import unittest
from is_prime import is_prime


class Test_is_prime(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(1))



if __name__ == "__main__":
    unittest.main()
