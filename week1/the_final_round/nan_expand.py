#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def nan_expand(times):
    nota = "Not a " * times
    return nota + "NaN" if times > 0 else ''

if __name__ == "__main__":
    print (nan_expand(5))
