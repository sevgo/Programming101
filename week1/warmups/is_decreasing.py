#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_decreasing(seq):
    for element in range(0, len(seq) - 1):
        if seq[element] < seq[element + 1]:
            return False

    return True


if __name__ == "__main__":
    print (is_decreasing([6, 5, 4, 3, 1]))
