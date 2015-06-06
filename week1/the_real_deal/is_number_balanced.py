#!/usr/bin/env python3

from to_digits import to_digits

def is_number_balanced(n):
    digits = to_digits(n)
    med = len(digits) // 2
    if len(digits) % 2 == 0:
        m = med
    else:
        m = med + 1

    return sum(digits[0:med]) == sum(digits[m:])

if __name__ == "__main__":
    print (is_number_balanced(5234))
