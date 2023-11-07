#!/usr/bin/python3
"""0-nqueens.py - N queens"""

from sys import argv

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    N = int(argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if N < 4:
    print('N must be at least 4')
    exit(1)


def solve_nqueens(n):
    '''self descriptive'''
    if n == 0:
        return [[]]
    inner_solution = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(N)
            for solution in inner_solution
            if safe_queen((n, i + 1), solution)]


def attack_queen(square, queen):
    '''self descriptive'''
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr, queens):
    '''self descriptive'''
    for queen in queens:
        if attack_queen(sqr, queen):
            return False
    return True


for items in reversed(solve_nqueens(N)):
    result = []
    for item in [list(item) for item in items]:
        result.append([i - 1 for i in item])
    print(result)
