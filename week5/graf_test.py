#!/usr/bin/env python3
import unittest
from graf import Graph

class Test_Graph(unittest.TestCase):
    def setUp(self):
        self.gg = Graph()
        self.gg.add("sevgo")
        self.gg.add("nikpet")
        self.gg.add_edge("sevgo", "nik")
        self.gg.add_edge("sevgo", "vesela")
        self.gg.add_edge("vesela", "hristo")
        self.gg.add_edge("nik", "presko")
        self.gg.add_edge("presko", "nadya")
        self.gg.add_edge("nadya", "sevgo")

    def test_empty_graf(self):
        self.assertIsInstance(self.gg, Graph)

    def test_is_empty(self):
        self.assertFalse(self.gg.is_empty())

    def test_add_node(self):
        with self.assertRaises(Exception):
            self.gg.add("sevgo")

    def test_neighbours(self):
        self.gg.add_edge("sevgo", "nikpet")
        self.gg.add_edge("sevgo", "presianbg")
        self.gg.add_edge("radoy", "sevgo")
        self.assertGreater(len(self.gg.get_neighbors_for("sevgo")), 0)
        self.assertEqual(len(self.gg.get_neighbors_for("sevgo")), 6)
        self.assertIsInstance(self.gg.get_neighbors_for("sevgo"), list)

    def test_path_between(self):
        self.gg.add_edge("gosho", "presko")
        self.assertTrue(self.gg.path_between("sevgo", "nadya"))
        self.assertFalse(self.gg.path_between("sevgo", "gosho"))

if __name__ == "__main__":
    unittest.main()
