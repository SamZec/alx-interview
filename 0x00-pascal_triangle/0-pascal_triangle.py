#!/usr/bin/python3
"""0-pascal_triangle.py - a module for creating pascal triangle"""


def pascal_triangle(n):
    """Create pascal triangel of n level"""
    triangle = []
    if n > 0:
        for level in range(1, n + 1):
            level_angle = []
            angle = 1
            for row in range(1, level + 1):
                level_angle.append(angle)
                angle = angle * (level - row) // row
            triangle.append(level_angle)
    return triangle
