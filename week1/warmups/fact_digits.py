#!/usr/bin/env python3

from factorial import factorial


def fact_digits(number):
    summ = 0
    while number > 0:
        p = number % 10
        summ += factorial(p)
        number = number // 10

    return summ


if __name__ == "__main__":
    print (fact_digits(145))
