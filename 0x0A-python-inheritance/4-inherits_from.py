#!/usr/bin/python3
"""
A module containing one function:
    "inherits_from"
"""


def inherits_from(obj, a_class):
    """
    A function to check if an instance "obj" is an instance
    of a class that is inherited, directly or indirectly,
    by "a_class".

    Return: "True" if true, "False" if false
    """

    obj_class = type(obj)
    return issubclass(obj_class, a_class) and obj_class is not a_class:
