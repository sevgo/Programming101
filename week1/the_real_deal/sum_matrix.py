#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_matrix(n):
    """ Returns a sum of all elements in a
    given matrix """
    
    return sum([sum(x) for x in n])


if __name__ == '__main__':
    print (sum_matrix([[0, 3, 0], [0, 4, 0], [0, 13, 0]]))
