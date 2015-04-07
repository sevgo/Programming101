#!/usr/bin/env python3
import json
from datetime import time
from random import randint
from copy import deepcopy

class Song:

    """ Class that represents a mp3 encoded music file """

    def __init__(self, title="", artist="", album="", length=""):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __to_hours(self, length):
        t = length.split(':')
        if 3 == len(t):
            return int(t[0])

        return 0

    def __to_minutes(self, length):

        t = length.split(':')
        if 3 == len(t):
            return (60 * int(t[0]) + int(t[1]))
        elif 2 == len(t):
            return int(t[0])

        return 0

    def __to_seconds(self, length):
        t = length.split(':')
        if 3 == len(t):
            return (3600 * int(t[0]) + 60 * int(t[1]) + int(t[2]))
        elif 2 == len(t):
            return int(60 * int(t[0]) + int(t[1]))

        return int(t[0])

    def _length(self, hours=False, minutes=False, seconds=False):

        if hours:
            return self.__to_hours(self.length)
        elif minutes:
            return self.__to_minutes(self.length)
        elif seconds:
            return self.__to_seconds(self.length)

        return str(self.length)

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title,
                                             self.album, self.length)

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


class Playlist:
    """ A playlist class """
    def __init__(self, name="PlayListName", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self._playlist = []
        self.__current_song = None
        self.__playing = []

    def add_song(self, song):
        """Adds a song to the playlist."""
        if not isinstance(song, Song):
            raise TypeError("It's not a Song object!")

        self._playlist.append(song)
        self.__playing = deepcopy(self._playlist)

    def remove_song(self, song):
        """If there is such song in the playlist deletes it."""
        if not isinstance(song, Song):
            raise TypeError("It's not a Song object!")

        if song not in self._playlist:
            raise ValueError("There's not such a song in the playlist!")

        self._playlist.remove(song)

    def add_songs(self, songs):
        """Adds list of songs to the playlist."""
        if type(songs) != list:
            raise TypeError("List object expected!")

        for song in songs:
            if not isinstance(song, Song):
                raise TypeError("Objects ot type Song expected!")

        self._playlist += songs
        self.__playing = deepcopy(self._playlist)

    def __humanize(self, secs):
        mins, secs = divmod(secs, 60)
        hours, mins = divmod(mins, 60)

        return "%02d:%02d:%02d" % (hours, mins, secs)

    def total_length(self):
        seconds = 0
        for song in self._playlist:
            seconds += song._length(seconds=True)

        return self.__humanize(seconds)

    def artists(self):
        artists_histogram = {}
        for song in self._playlist:
            if song.artist not in artists_histogram:
                artists_histogram[song.artist] = 1
            else:
                artists_histogram[song.artist] += 1

        return artists_histogram
        
    def __random_song(self, tmplaylist):
        max_songs = len(tmplaylist)
        return randint(0, max_songs)

    def _play_song(self):
        print(self.__playing)
        track_number = self.__random_song(self.__playing)
        if self.shuffle:
            self.__current_song = self.__playing.pop(track_number)

        self.__current_song = self.__playing.pop(0)

    def next_song(self):
        if 0 == len(self.__playing) and self.repeat:
            self.__playing = deepcopy(self._playlist)
            self._play_song()

        if self.shuffle:
            track_number = self.__random_song(self.__playing)
            return self.__playing.pop(self.__playing.index(track_number))

if __name__ == "__main__":
    hideaway = Song(
        title="Hideaway", artist="Kiesza", album="Hideaway", length="4:34")
    print(hideaway._length())
