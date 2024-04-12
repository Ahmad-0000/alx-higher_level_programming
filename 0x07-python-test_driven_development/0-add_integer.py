#!/usr/bin/python3
"""
A module containing one function:
    "add_integer"
"""


def add_integer(a, b=98):
    """
    A function to return the reslut of "a" + "b"
    with input validation first.
    """

    allowed_types = [int, float]
    if type(a) not in allowed_types:
        raise TypeError('a must be an integer')
    elif type(b) not in allowed_types:
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return (a + b)
