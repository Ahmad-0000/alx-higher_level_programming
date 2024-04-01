#!/usr/bin/python3
""" A module containing
    one function, add_integer,
    which can be used
    to return the sum of two
    integers after ensuring their types"""


def add_integer(a, b=98):
    """         to return a + b - if they are
        integers, floats or mixed-
        errors are raised otherwise """
    allowed_types = [int, float]
    if type(a) not in allowed_types:
        raise TypeError('a must be an integer')
    elif type(b) not in allowed_types:
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return (a + b)
