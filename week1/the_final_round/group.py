#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from copy import deepcopy


def group(src):
    """ Method that takes a list of elements
    and returns a list of groups of elements
    if there are equal lements that can be
    groupped """


    dst = []
    tmp = []
    tmp.append(src.pop(0))
    llen = len(src)
    while llen > 0:
        if src[0] in tmp:
            tmp.append(src.pop(0))
        else:
            dst.append(tmp)
            tmp = []
            tmp.append(src.pop(0))
        # lenght of the source list is decreasing
        # with every step
        llen = len(src)
    # when llen become equal to 0 tmp still
    # contains the last group of elements
    # so we append it to dst
    dst.append(tmp)

    return dst


if __name__ == '__main__':
    source = [1, 2, 2, 3, 1, 1, 1]
    print (group(source))
