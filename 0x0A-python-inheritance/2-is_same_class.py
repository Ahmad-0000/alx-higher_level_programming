#!/usr/bin/python3
"""
A module containing one function:
    "is_same_class"
"""


def is_same_class(obj, a_class):
    """
    A function to check whether an instance "obj" is
    a direct subclass of "a_class"
    """

    if isinstance(obj, a_class) and f"{type(obj)}" == f"{a_class}":
        return True
    return False
