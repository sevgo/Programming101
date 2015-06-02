#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

from sum_of_divisors import sum_of_divisors

def is_prime(n):
    # If N is prime it could only be devided 
    # to 1 and N, so sum of divisors has to be 
    # equal to N + 1
    return n + 1 == sum_of_divisors(n)


if __name__ == "__main__":
    number = int(input("Number: "))
    print (is_prime(number))
