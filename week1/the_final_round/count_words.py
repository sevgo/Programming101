#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count_words(arr):
    """Counts words in a list and returns a dictionary
    of the type {"word":count} """
    unique = set(arr)
    words = {}
    for element in unique:
        words[element] = 0

    for el in unique:
        for e in arr:
            if e == el:
                words[el] += 1

    return words


if __name__ == "__main__":
    print (count_words(["ala", "bala", "ala", "store", "new", "key", "new"]))
