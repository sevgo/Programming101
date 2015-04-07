#!/usr/bin/env python3
import unittest
from jukebox import Song, Playlist


class Test_JukeBox(unittest.TestCase):

    def setUp(self):
        self.hideaway = Song(title="Hideaway", artist="Kiesza",
                             album="Hideaway", length="4:34")
        self.summer = Song(title="Summer", length="3:13",
                           artist="Calvin Harris")
        self.hd = Song(title="Hideaway", artist="Kiesza",
                             album="Hideaway", length="4:34")

        manowar_hail = Song(title="Hail and Kill", artist="manowar",
                            album="Kings of Metal", length="5:59")
        manowar_heart = Song(title="Heart of Steal", artist="manowar",
                             album="Kings of Metal", length="5:10")
        manowar_blood = Song(title="Blood of the Kings", artist="manowar",
                             album="Kings of Metal", length="7:30")
        songs = [self.hd, manowar_heart, manowar_hail, manowar_blood,
                 self.summer]
        self.playlist = Playlist(name="misc.pl")

        self.playlist.add_songs(songs)

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
        self.assertEqual(hash(self.hideaway),
                         hash("Kiesza - Hideaway from Hideaway - 4:34"))

    def test_same_song(self):
        self.assertNotEqual(self.hideaway, self.summer)
        self.assertFalse(self.summer == self.hideaway)
        self.assertTrue(self.hd == self.hideaway)

    def test_is_it_playlist_object(self):
        self.assertIsInstance(self.playlist, Playlist)
        self.assertTrue(self.playlist.name == "misc.pl")

    def test_adding_song_to_playslist(self):
        # self.playlist.add_song(self.hideaway)
        self.assertEqual(self.hideaway, self.playlist._playlist[0])
        with self.assertRaises(TypeError):
            self.playlist.add_song("TestSong")

    def test_removing_song_from_playlist(self):
        self.playlist = Playlist(name="mic.pl")
        self.playlist.add_song(self.hideaway)
        with self.assertRaises(ValueError):
            self.playlist.remove_song(self.summer)

    def test_adding_songs_to_playlist(self):
        with self.assertRaises(TypeError):
            self.playlist.add_songs({"Track1": "Unknown", "Track2": "Known"})
        self.playlist.add_songs([self.summer, self.hideaway])

    def test_playlist_length(self):
        self.playlist.add_songs([self.summer, self.hideaway])
        self.assertIsInstance(self.playlist.total_length(), str)

    def test_artists(self):
        self.assertIsInstance(self.playlist.artists(), dict)
        self.assertEqual(self.playlist.artists()['manowar'], 3)

    def test_next_song(self):
        self.playlist._play_song()
        curr_s = self.playlist.next_song()
        next_s = self.playlist.next_song()
        next_next = self.playlist.next_song()
        self.assertFalse(curr_s == next_next())

if __name__ == '__main__':
    unittest.main()
