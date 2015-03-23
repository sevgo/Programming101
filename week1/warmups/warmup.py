# -*- coding: utf-8 -*-


def factoriel(n):
    """ Calculates factoriel of give number
       that uses a recursion """
    if n == 0:
        return 1

    return n * factoriel(n-1)


def fibonacci(n):
    fib = [1, 1]
    if n <= 2:
        return fib
    for num in range(2, n):
        x = fib[num-1] + fib[num-2]
        fib.append(x)
    return fib


def sum_of_digits(number):
    """ A function that takes an integer and
    calculates the sum of n's digits """
    number = abs(number)
    summ = 0
    p = 0
    if number < 9:
        return number

    while number > 0:
        p = number % 10
        summ += p
        number = number // 10

    return summ


def fact_digits(number):
    summ = 0
    while number > 0:
        p = number % 10
        summ += factoriel(p)
        number = number // 10

    return summ


def palindrome(obj):
    string = str(obj)
    string2 = ""
    string3 = ""
    string = string.lower()
    for index in range(0, len(string)):
        if string[index].isalnum():
            string2 = string2 + string[index]

    for index in range(len(string2) - 1, -1, -1):
        string3 += string2[index]

    if string2 == string3:
        return True
    else:
        return False

if __name__ == "__main__":
    print (palindrome("121"))
