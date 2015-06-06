#!/usr/bin/env python3

import unittest
from is_number_balanced import is_number_balanced


class Test_is_balanced(unittest.TestCase):

    def test_is_balanced(self):
        self.assertTrue(is_number_balanced(5234))
        self.assertFalse(is_number_balanced(10546))



if __name__ == "__main__":
    unittest.main()
