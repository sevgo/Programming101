#!/usr/bin/env python3

def to_number(digits):
    """ Function which takes a list of integers - digits
    and returns the number, containing those digits """
    p = 0
    for n in digits:
        multiplier = 10 ** len(str(n))
        p *= multiplier
        p = p + int(n)

    return p


if __name__ == "__main__":
    print (to_number([9,9,90,9,9]))
