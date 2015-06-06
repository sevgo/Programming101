#!/usr/bin/env python3

import unittest
from prime_number_of_divisors import prime_number_of_divisors as pn_d


class Test_prime_num_divisors(unittest.TestCase):

    def test_prime_num_divisors(self):
        number = 89
        self.assertTrue(pn_d(number))

if __name__ == "__main__":
    unittest.main()
