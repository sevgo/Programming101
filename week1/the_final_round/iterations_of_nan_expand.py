#!/usr/bin/env python3
# -*- cofing: utf-8 -*-


from nan_expand import nan_expand
from count_words import count_words


def iterations_of_nan_expand(expanded):
    string = expanded.strip()
    if string.find("Not a NaN") < 0:
        return False
    return 0 if "" == string else string.count("Not a")


if __name__ == "__main__":
    print (iterations_of_nan_expand("Not a Not a Not a NaN"))
