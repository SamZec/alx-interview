#!/usr/bin/python3
"""0-pascal_triangle.py - a module for creating pascal triangle"""
from math import factorial as fact


def pascal_triangle(n):
    """Calculates and form pascal triangle of n level"""
    # check if n is zero
    if n <= 0:
        return []

    # create triangle container
    triangle = []
    # set initial level to 0
    level = 0

    # loop through level to n
    while (level < n):
        # create level triangle container
        l_angle = []
        # loop to create the triangle
        for j in range(level + 1):
            # append the formed triangle to level triangle cotainer
            l_angle.append(fact(level) // (fact(j) * fact(level - j)))

        # append level triangle to triangle
        triangle.append(l_angle)

        # update level
        level += 1
    # return triangle
    return triangle
