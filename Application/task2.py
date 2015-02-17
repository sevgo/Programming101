# Task2: Tetrahedron filled with water.
#
from task1 import fill_tetrahedron
import math


def get_volumes_sort(sides):
    vol = []
    if sides:
        for el in sides:
            elm = int(el)
            vol.append(fill_tetrahedron(elm))
    else:
        print ("List is empty!")
    vol.sort()
    return vol


if __name__ == "__main__":
    sides = input("Enter comma-separated elements of a list, please: ")
    sides = sides.split(",")
    print (sides)
    lst = get_volumes_sort(sides)
    print (lst)
