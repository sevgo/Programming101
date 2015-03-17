#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_of_digits(number):
    """ A function that takes an integer and
    calculates the sum of n's digits """

    summ = 0
    p = 0
    if number < 9:
        return number

    while number > 0:
        p = number % 10
        summ += p
        number = number // 10

    return summ


if __name__ == "__main__":
    print (sum_of_digits(12345))
