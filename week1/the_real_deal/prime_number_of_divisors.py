#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from is_prime import is_prime


def prime_number_of_divisors(n):
    return is_prime(len([x for x in range(1, n + 1) if n % x == 0]))


if __name__ == "__main__":
    number = 89
    print (prime_number_of_divisors(number))
