#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_of_divisors(n):
    return sum([x for x in range(1, n + 1) if n % x == 0])


if __name__ == "__main__":
    number = 11
    print ("Sum of divisors of %d is: %d" % (number, sum_of_divisors(number)))
