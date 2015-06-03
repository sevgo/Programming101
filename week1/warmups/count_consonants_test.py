#!/usr/bin/env python3

import unittest
from count_consonants import count_consonants


class Test_Consonants(unittest.TestCase):

    def test_count(self):
        self.assertEqual(count_consonants("MoNTHy PyTHoN"), 8)


if __name__ == "__main__":
    unittest.main()
