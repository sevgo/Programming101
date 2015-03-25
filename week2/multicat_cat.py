#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from cat import cat

def multi_cat(filename):
    """ Python implementation of cat command.
    It takes file name(s) as arguments and
    print files' content to standart output
    Please provide a filename to be catted """

    return cat(filename)

def main():
    if len(sys.argv) <= 1 or sys.argv[1] == "--help":
        print(multi_cat.__doc__)
    else:
        for fl in sys.argv[1:]:
            return multi_cat(fl)


if __name__ == "__main__":
    str = main()
    print(str)
