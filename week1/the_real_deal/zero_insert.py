#!/usr/bin/env python3

from to_digits import to_digits
from to_number import to_number


def zero_insert(n):
    p = []
    number = to_digits(n)
    p.append(number[0])
    x = 0
    while x < len(number) - 1:
        if number[x] == number[x+1] or (number[x]+number[x+1]) % 10 == 0:
            p.append(0)

        p.append(number[x+1])
        x += 1
    return to_number(p)

if __name__ == '__main__':
    print (zero_insert(116457))

