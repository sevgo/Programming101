#!/usr/bin/env python3

import unittest
from max_consecutive import max_consecutive


class Test_max_consecutive(unittest.TestCase):

    def test_max_consecutive(self):
        self.asserEqual(max_consecutive([9, 6, 6, 3, 3, 5, 5, 5, 5, 5, 5]), 6)



if __name__ == "__main__":
    unittest.main()
