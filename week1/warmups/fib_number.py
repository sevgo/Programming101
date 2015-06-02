#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fibonacci import fibonacci
from to_number import to_number


def fib_number(n):
    """ Function which takes an integer n and returns a number,
    which is formed by concatenating the first n Fibonacci numbers """
    digits = fibonacci(n)
    number = to_number(digits)
    print (digits)
    print (number)

fib_number(3)
