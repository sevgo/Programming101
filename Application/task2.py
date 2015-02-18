#!/usr/bin/env python3
# Task2: Tetrahedron filled with water.
#
from task1 import fill_tetrahedron
import math


def get_volumes_sorted(sides):
    """Calculates volumes of regular tetrahedrons
    by given list of their sides and return a sorted
    list of calculated volumes"""

    vol = []
    if sides:
        for el in sides:
            elm = int(el)
            vol.append(fill_tetrahedron(elm))
    else:
        print ("List is empty!")
        return None
    vol.sort()
    return vol


def tetrahedron_filled(tetrahedrons, water):
    """It count how many tetrahedrons you can 
    fill with "water" liters of water"""

    if not tetrahedrons:
        print ("No tetrahedrons were provided!")
        return None
    else:
        tetrahedrons_counter = 0
        volumes = get_volumes_sorted(tetrahedrons)
        summ_volumes = sum(float(vol) for vol in volumes)
        if volumes:
            if water >= summ_volumes:
                tetrahedrons_counter = len(volumes)
            else:
                for element in volumes:
                    if element > water:
                        break
                    else:
                        tetrahedrons_counter += 1
                        water -= element

    return tetrahedrons_counter


if __name__ == "__main__":
    #sides = input("Enter comma-separated elements of a list, please: ")
    #sides = sides.split(",")
    print (tetrahedron_filled([110, 210, 186, 97, 105], 2100))
