#!/usr/bin/env python3

from fibonacci import fibonacci
from to_number import to_number


def fib_number(n):

    """ Function which takes an integer n and returns a number,
    which is formed by concatenating the first n Fibonacci numbers """

    digits = fibonacci(n)
    number = to_number(digits)

    return number
