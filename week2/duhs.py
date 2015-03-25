#!/usr/bin/env python3
import sys
from os import walk
from os.path import getsize, normpath, join


def duhs(path):
    """
    """

    files = []
    size = 0
    for root, dirnames, filenames in walk(path):
        print(root)
        print(dirnames)
        print(filenames)
        for element in filenames:
            files.append(join(root, element))

    for element in files:
        print(element)
        fsize = int(getsize(element))
        print (fsize)
        size += fsize
        #print("Size: %d" % size)

    return size


def main():

    if len(sys.argv) <= 1 or sys.argv[1] == "--help":
        print(duhs.__doc__)
    else:
        path = normpath(sys.argv[1])
        return duhs(path)

if __name__ == "__main__":
    print("Total size: %d" % main())
