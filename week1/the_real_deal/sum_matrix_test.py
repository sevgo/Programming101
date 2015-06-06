#!/usr/bin/env python3

import unittest
from sum_matrix import sum_matrix


class Test_sum_matrix(unittest.TestCase):

    def setUp(self):
        self.matrix = [[0, 3, 0], [1, 2, 1], [0, 6, 7]]

    def test_sum_matrix_result(self):
        self.assertTrue(20 == sum_matrix(self.matrix))

    def test_sum_matrix_type(self):
        self.assertIsInstance(sum_matrix(self.matrix), int)


if __name__ == "__main__":
    unittest.main()
