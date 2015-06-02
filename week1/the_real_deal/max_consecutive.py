#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from group import group


def max_consecutive(items):
    return max([len(x) for x in group(items)])


if __name__ == '__main__':
    ls = [9, 6, 6, 6, 3, 3, 5, 5, 5, 5, 5]
    print (max_consecutive(ls))
