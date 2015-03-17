#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from factoriel import factoriel


def fact_digits(number):
    summ = 0
    while number > 0:
        p = number % 10                                                         
        summ += factoriel(p)
        number = number // 10                                                   

    return summ


if __name__ == "__main__":
    print (fact_digits(145))
