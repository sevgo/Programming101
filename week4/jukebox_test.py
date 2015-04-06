#!/usr/bin/env python3
import unittest
from jukebox import Song


class Test_JukeBox(unittest.TestCase):

    def setUp(self):
        self.hideaway = Song(title="Hideaway", artist="Kiesza",
                             album="Hideaway", length="4:34")
        self.summer = Song(title="Summer", length="3:13",
                           artist="Calvin Harris")
        self.hd = Song(title="Hideaway", artist="Kiesza",
                             album="Hideaway", length="4:34")

    def test_is_it_song(self):
        self.assertIsInstance(self.hideaway, Song)

    def test_length(self, minutes=True):
        self.assertEqual(self.hideaway._length(minutes=True), 4)
        self.assertEqual(self.hideaway._length(hours=True), 0)
        self.assertEqual(self.hideaway._length(seconds=True), 274)
        self.assertEqual(self.hideaway._length(), "4:34")
        self.assertIsInstance(self.hideaway._length(), str)

    def test__str__(self):
        self.assertIsInstance(self.hideaway.__str__(), str)
        self.assertEqual(
            str(self.hideaway), "Kiesza - Hideaway from Hideaway - 4:34")

    def test_is_hashable(self):
        self.assertEqual(
            hash(self.hideaway), hash("Kiesza - Hideaway from Hideaway - 4:34"))

    def test_same_song(self):
        self.assertNotEqual(self.hideaway, self.summer)
        self.assertFalse(self.summer == self.hideaway)
        self.assertTrue(self.hd == self.hideaway)


if __name__ == '__main__':
    unittest.main()
