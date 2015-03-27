#!/usr/bin/env python3
# -*- coding utf-8 -*-
from group import group


def is_an_bn(word):
    word_lst = [ch for ch in word]
    groupped = group(word_lst)
    if len(groupped) > 2 or len(groupped[0]) != len(groupped[1]):
        return False
    else:
        a = set(groupped[0])
        b = set(groupped[1])
        if 'a' not in a or 'b' not in b:
            return False

    return True


if __name__ == "__main__":
    print (is_an_bn("aaaaabbbbb"))
