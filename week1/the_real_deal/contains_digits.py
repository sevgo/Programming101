#!/usr/bin/env python3

from contains_digit import contains_digit


def contains_digits(number, digits):
    for n in digits:
        if not contains_digit(number, n):
            return False

    return True

if __name__ == "__main__":
    print (contains_digits(124167, [1, 4, 9]))
