#!/usr/bin/env python3

import unittest
from count_substrings import count_substrings


class Test_substring_count(unittest.TestCase):

    def test_substrings_count(self):
        sub = "yth"
        string = "Python myth is yet another myth but wyth a python"
        self.assertIsInstance(count_substrings(string, sub), int)
        self.assertEqual(count_substrings(string, sub), 5)


if __name__ == "__main__":
    unittest.main()
