#!/usr/bin/env python3
# -*- cofing: utf-8 -*-
from nan_expand import nan_expand
from count_words import count_words


def iterations_of_nan_expand(expanded):
    string = expanded.strip()
    exp = set(expanded.strip().split())
    org = {'Not', 'a', 'NaN'}
    if len(exp.difference(org)) > 0:
        print ("Given string is not valid NaN string")
        return False
    else:
        return 0 if "" == string else string.count("Not a")


if __name__ == "__main__":
    print (iterations_of_nan_expand("Not a Not a Not a NaN "))
