#!/usr/bin/env python3
import json
from datetime import time


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

    def add_song(self, song):
        if not isinstance(song, Song):
            raise TypeError("It's not a Song object!")

        self._playlist.append(song)


if __name__ == "__main__":
    hideaway = Song(
        title="Hideaway", artist="Kiesza", album="Hideaway", length="4:34")
    print(hideaway._length())
