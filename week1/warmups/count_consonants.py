#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count_consonants(string):
    """ Function which returns the count of 
    all consonants in the string \"string\" """
    consonants = "bcdfghjklmnpqrstvwxz"
    counter = 0
    if string:
        for ch in string.lower():
            if ch in consonants:
                counter += 1

    return counter


if __name__ == "__main__":
    strng = "MOnty PYthon!"
    print ("%s contains %d consonants" % (strng, count_consonants(strng)))
