#!/usr/bin/env python3


def is_increasing(seq):
    for element in range(0, len(seq) - 1):
        if seq[element] > seq[element + 1]:
            return False

    return True
