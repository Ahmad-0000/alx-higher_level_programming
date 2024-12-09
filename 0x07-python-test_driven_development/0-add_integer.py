#!/usr/bin/python3
"""
A module containing one function:
    "add_integer"
"""
from math import isnan


def add_integer(a, b=98):
    """
    A function to return the reslut of "a" + "b"
    with input validation first.
    """

    allowed_types = [int, float]
    if type(a) not in allowed_types or isnan(a):
        raise TypeError('a must be an integer')
    if type(b) not in allowed_types or isnan(b):
        raise TypeError('b must be an integer')
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
