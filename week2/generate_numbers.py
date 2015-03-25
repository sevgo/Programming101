#!/usr/bin/env python3
import sys
from random import randint


def generate_numbers(filename, n):
    """
    @filename: a file where generated numbers will be written
    @n: how much random numbers it should generate
    @Description: generates "n" random integers and write
    them down to filename
    """

    with open(filename, 'w') as fd:
        for index in range(0, n + 1):
            fd.write(" ".join(str(randint(1, 1000))))


def main():

    if len(sys.argv) <= 2 or sys.argv[1] == "--help":
        print(generate_numbers.__doc__)
    else:
        generate_numbers(sys.argv[1], int(sys.argv[2]))


if __name__ == "__main__":
    main()
