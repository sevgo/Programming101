#!/usr/bin/env python3


def fibonacci(n):
    fib = [1, 1]
    if n <= 2:
        return fib

    for num in range(2, n):
        x = fib[num-1] + fib[num-2]
        fib.append(x)

    return fib


if __name__ == "__main__":
    print(fibonacci(10))
