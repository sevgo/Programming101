#!/usr/bin/env python3


import unittest
from count_vowels import count_vowels


class Test_Vowels(unittest.TestCase):

    def test_counter(self):
        self.assertEqual(count_vowels("mOnthY pYthOn"), 4)


if __name__ == "__main__":
    unittest.main()
