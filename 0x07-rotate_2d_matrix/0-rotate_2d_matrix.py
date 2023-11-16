#!/usr/bin/python3
"""0-rotate_2d_matrix.py - Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """rotate 2D matrix 90 degrees clockwise"""
    _len = len(matrix)
    index = 0
    for row in range(_len):
        temp = []
        for column in range(_len):
            temp.append(matrix[-(column+1)][row])
        matrix.insert(index, temp)
        index += 1
    del matrix[index:]
