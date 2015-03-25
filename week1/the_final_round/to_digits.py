#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def to_digits(n):
    """Takes an integer n and returns a list, containing the digits of n."""
    digitsList = []
    while n > 0:
        digitsList.append(n % 10)
        n = n // 10

    digitsList.reverse()
    return digitsList


if __name__ == "__main__":
    print (to_digits(99999))
