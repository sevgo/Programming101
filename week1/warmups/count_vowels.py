#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count_vowels(string):
    """ Function which returns the count of all vowels in the string str """
    vowels = "aeiouy"
    counter = 0
    if string:
        for ch in string.lower():
            if ch in vowels:
                counter += 1

    return counter


if __name__ == "__main__":
    strng = "MOnty PYthon"
    print ("%s contains %d vowels" % (strng, count_vowels(strng)))
