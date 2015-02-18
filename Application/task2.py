# Task2: Tetrahedron filled with water.
#
from task1 import fill_tetrahedron
import math


def get_volumes_sorted(sides):
    vol = []
    if sides:
        for el in sides:
            elm = int(el)
            vol.append(fill_tetrahedron(elm))
    else:
        print ("List is empty!")
    vol.sort()
    return vol


def get_sum_volumes(volumes):
    return sum(float(vol) for vol in volumes)


def tetrahedron_filled(tetrahedrons, water):
    tetrahedrons_counter = 0
    volumes = get_volumes_sorted(tetrahedrons)
    if volumes:
        if water >= get_sum_volumes(volume):
            tetrahedrons_counter = volumes.len()
        else:
            for element in volumes:
                if element <= water


if __name__ == "__main__":
    sides = input("Enter comma-separated elements of a list, please: ")
    sides = sides.split(",")
    print (sides)
    lst = get_volumes_sort(sides)
    print (lst)
