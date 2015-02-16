# Task1: Fill tetrahedron with water
import math


def fill_tetrahedron(num):
    """ A method that takes an integer as argument
    (which is the side of a regular tetrahedron)
    and calculates how much water do you need to fill
    a regular tetrahedron"""

    if num <= 0:
        print ("Please provide a positive integer!")
        return False
    else:
        return ((math.pow(num, 3) * math.sqrt(2)) / 12) / 1000



if __name__ == "__main__":
    try:
        number = int(input("Plese, enter an integer: "))
        print (fill_tetrahedron(number))
    except ValueError:
        print ("Sorry, it was not a valid number")
