#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sum_matrix import sum_matrix
from copy import deepcopy


def move_down(rows, t):
    """ A method that takes number of rows in the matrix
    and coordinates of bomb's position and returns
    coordinates of neighbour located bellow the bomb.
    It returns None if there isn't such a neighbour """

    x, y = t
    if x == rows:
        return None
    else:
        return (x + 1, y)


def move_up(t):
    """ A method that takes coordinates of bomb's
    position and returns coordinates of neighbour
    located above the bomb. It returns None if
    there isn't such a neighbour """

    x, y = t
    if x == 0:
        return None
    else:
        return (x - 1, y)


def move_left(t):
    """ A method that takes coordinates of bomb's
    position and returns coordinates of neighbour
    located at the left of the bomb. It returns None
    if there isn't such a neighbour """

    x, y = t
    if y == 0:
        return None
    else:
        return (x, y - 1)


def move_right(columns, t):
    """ A method that takes coordinates of bomb's position
    and number of columns and returns coordinates of
    neighbour located at the right of the bomb. It returns
    None if there isn't such a neighbour """

    x, y = t
    if y == columns:
        return None
    else:
        return (x, y + 1)


def move_up_right(columns, t):
    """ A method that takes number of columns of the matrix
    and coordinates of the bomb and returns coordinates of
    neighbour which is located at the right-hand side and
    above the bomb. It returns None if there isn't such a
    neighbour """

    x, y = t
    if x == 0 or y == columns:
        return None
    else:
        return (x - 1, y + 1)


def move_up_left(t):
    """ A method that takes coordinates of the bomb and
    returns coordinates of neighbour which is located at
    the left-hand side and above the bomb. It returns
    None if there isn't such a neighbour """

    x, y = t
    if x == 0 or y == 0:
        return None
    else:
        return (x - 1, y - 1)


def move_down_left(rows, columns, t):
    """ A method that takes coordinates of the bomb, number
    of rows and number of columns of the matrix and
    returns coordinates of neighbour which is located at
    the left-hand side and bellow the bomb. It returns None
    if there isn't such a neighbour """

    x, y = t
    if x == rows or y == 0:
        return None
    else:
        return (x + 1, y - 1)


def move_down_right(rows, columns, t):
    """ A method that takes coordinates of the bomb, number
    of rows and number of columns of the matrix and
    returns coordinates of neighbour which is located at
    the right-hand side and bellow the bomb. It returns None
    if there isn't such a neighbour """

    x, y = t
    if x == rows or y == columns:
        return None
    else:
        return (x + 1, y + 1)


def find_neighbour(matrix, position):
    """ Put a bomb in a matrix and calculates damages.
    It returns a new copy of the matrix wich contains
    the new values after the explosion. """

    # It's important to clone the matrix before do anything else
    new_matrix = deepcopy(matrix)
    x, y = position
    bomb = matrix[x][y]
    rows = len(new_matrix) - 1
    columns = len(new_matrix[0]) - 1
    # Find neighbours of bomb's position
    moves = [move_up(position),
             move_down(rows, position),
             move_left(position),
             move_right(columns, position),
             move_up_right(columns, position),
             move_up_left(position),
             move_down_right(rows, columns, position),
             move_down_left(rows, columns, position)]

    neighbours = [z for z in moves if z is not None]
    ## Calculating damages and returning the new matrix
    #  after the explosion
    for element in neighbours:
        x, y = element
        new_value = new_matrix[x][y] - bomb
        new_matrix[x][y] = new_value if new_value >= 0 else 0

    return new_matrix


def matrix_bombing_plan(m):
    """ This method calculates sum of the matrix by
    trying every possible position of the bomb and
    returns a dictionary. Dictionary's keys are the
    positions of the bomb and values are the sums of
    the matrix after the damage """
    matrix = deepcopy(m)

    rows = len(m)
    columns = len(m[0])
    d = {}
    for x in range(0, rows):
        for y in range(0, columns):
            p = (x, y)
            neighbours = find_neighbour(matrix, (x, y))
            d[p] = sum_matrix(neighbours)

    return d

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print (matrix_bombing_plan(matrix))
