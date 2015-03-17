#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# We cannot use math.factorial(n) I guess 

def factorial(n):
    """ Calculates factoriel of give number
       that uses a recursion """
    if n == 0:
        return 1

    return n * factorial(n-1)


if __name__ == "__main__":
    print (factorial(6))
