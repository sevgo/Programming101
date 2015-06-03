#!/usr/bin/env python3


def char_histogram(string):
    """ funcion which takes a string and returns a dictionary, where
    each key is a character from string and its value is the number
    of occurrences of that char in string. """
    histogram = {}
    for ch in string:
        if ch not in histogram:
            histogram[ch] = 1
        else:
            histogram[ch] += 1

    return histogram


if __name__ == "__main__":
    print (char_histogram("Monty Python!"))
