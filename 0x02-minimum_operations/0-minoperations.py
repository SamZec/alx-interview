#!/usr/bin/python3
"""0-minoperations.py - a module for the function minOperations(n)"""


def minOperations(n):
    """
        a method that calculates the fewest number of operations needed to
        result in exactly n H characters in a file.
    """
    if n <= 1:
        return 0

    for operations in range(2, n + 1):
        if n % operations == 0:
            return minOperations(int(n / operations)) + operations
