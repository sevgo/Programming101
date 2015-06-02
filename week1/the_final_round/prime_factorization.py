#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from is_prime import is_prime


def primes_list(number):
    return [x for x in range(2, number + 1) if is_prime(x)]


#def pow_tuple(t=(1, 1)):
#    return t[0] ** t[1]


#def mul_tuples(p1=(p1, a1), p2=(p2, a1)):
#    return p1 * p2


def prime_factorization(n):
    primes = primes_list(n)
    a = 1

if __name__ == "__main__":
    N = 25
    print (primes_list(N))
    print (prime_factorization(N))
