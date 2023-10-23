#!/usr/bin/python3
"""0-validate_utf8.py - module for validUTF8(data) function"""


def validUTF8(data):
    """
        determines if a given data set represents a valid UTF-8 encoding.

        args:
            data - list of integers

        Return:
            True if data is a valid UTF-8 encoding
            else False
    """
    data = iter(data)
    for leading_byte in data:
        leading_ones = count_leading_ones(leading_byte)
        if leading_ones in [1, 7, 8]:
            return False        # Illegal leading byte
        for _ in range(leading_ones - 1):
            trailing_byte = next(data, None)
            if trailing_byte is None or trailing_byte >> 6 != 0b10:
                return False    # Missing or illegal trailing byte
    return True


def count_leading_ones(byte):
    """checks for leading ones of byte"""
    for i in range(8):
        if byte >> (7 - i) == 0b11111111 >> (7 - i) & ~1:
            return i
    return 8
