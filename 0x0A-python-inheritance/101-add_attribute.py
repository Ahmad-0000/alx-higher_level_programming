#!/usr/bin/python3
"""
A module containg one function:
    "add_attribute"
"""


def add_attribute(obj, name, value):
    """ The code is easy to understand
    """

    not_allowed = [int, str, float, bool, None, dict,
                   list, set, tuple, complex]
    if type(obj) not in not_allowed and\
        ("__slots__" not in dir(obj) or name in obj.__slots__):
        obj.name = value
    else:
        raise TypeError("can't add new attribute")
