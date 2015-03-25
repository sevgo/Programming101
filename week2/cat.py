#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def cat(file_name):
    with open(file_name, 'r') as fd:
        return fd.read()


def main():
    """ Python implementation of cat command.
    It takes file name as first argument and
    print file's content to standart output
    Please provide a filename to be catted """

    if len(sys.argv) <= 1 or sys.argv[1] == "--help":
        print(cat.__doc__)
    else:
        return(cat(sys.argv[1]))

if __name__ == "__main__":
    main()
