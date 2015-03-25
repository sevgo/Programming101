#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

def reduce_file_path(path):
    path_str = path.lstrip("/").rstrip("/")
    path_lst = [x for x in path_str.split("/") if x not in ['/', '', '.']]
    tmp_curr = ''
    tmp_next = ''
    reduce_path = []
    plen = len(path_lst)
    for index in range(0, plen):
        element = path_lst[index]
        if element != "..":
            reduce_path.append(element)
        else:
            del reduce_path[len(reduce_path) - 1]

    return "/" + "/".join(reduce_path)


if __name__ == "__main__":
    path_to_reduce = "/home/./radorado/code//hackbulgaria/./week0/../../"
    print ("Given PATH: %s" % path_to_reduce)
    print ("Reduced PATH: %s" % reduce_file_path(path_to_reduce))
