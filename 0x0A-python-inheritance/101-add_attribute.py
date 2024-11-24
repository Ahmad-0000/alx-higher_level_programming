#!/usr/bin/python3
"""
A module containg one function:
    "add_attribute"
"""


def add_attribute(obj, name, value):
    """ The code is easy to understand
    """

    if "__slots__" not in dir(obj) or name in obj.__slots__:
        obj.name = value
    else:
        raise TypeError("can't add new attribute")
