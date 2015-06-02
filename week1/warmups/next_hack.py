#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from palindrome import palindrome


def is_hack_number(n):
    string = bin(n)[2:]
    is_odd = False
    if string.count('1') % 2 != 0:
        is_odd = True

    return palindrome(string) and is_odd


def next_hack(n):
    while not is_hack_number(n):
        n += 1

    return n

if __name__ == "__main__":
    n = 22
    print ("%d is hack_number: %s" % (n, is_hack_number(n)))
    print (next_hack(n))
