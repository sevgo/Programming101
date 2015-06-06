#!/usr/bin/env python3

def contains_digit(number, digit):
    return str(digit) in str(number)

if __name__ == "__main__":
    print (contains_digit(124167, 8))
