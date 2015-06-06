#!/usr/bin/env python3

import unittest
import bomberman as bman


class Test_Bomberman(unittest.TestCase):

    def setUp(self):
        self.matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]
        self.current_position = (2, 1)


    def test_move_up(self):
        self.assertIsInstance(bman.move_up(self.current_position), tuple)

    def test_value_of_new_position(self):
        x, y = bman.move_up(self.current_position)
        self.assertEqual(self.matrix[x][y], 5)

    def test_final_result_type(self):
        self.assertIsInstance(bman.matrix_bombing_plan(self.matrix), dict)


if __name__ == "__main__":
    unittest.main()
