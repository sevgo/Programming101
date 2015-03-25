#!/usr/bin/env python3
import sys


def sum_numbers(filename):
    """
    @filename: file that must contain numbers separated by " "
    @Description: returns sum of numbers in the file given
        as first argument
    """

    fd = open(filename, 'r')
    line = fd.read()
    fd.close()
    numbers_list = [int(x) for x in line.split()]
    return sum(numbers_list)


def main():
    if len(sys.argv) <= 1 or sys.argv[1] == "--help":
        print(sum_numbers.__doc__)
    else:
        return sum_numbers(sys.argv[1])


if __name__ == "__main__":
    print(main())
