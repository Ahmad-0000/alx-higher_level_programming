#!/usr/bin/python3
"""
A module containg one function:
    "add_attribute"
"""


def add_attribute(obj, name, value):
    """
    A function to add a new attribute to an
    object "obj" if "obj" is not an object
    of the classes "int", "str", "bool",
    "complex", "float", "set", "list",
    "dict" and "tuple", otherwise, an
    exception will arise with the message:
    "TypeError: can't add new attribute"
    """

    not_allowed_cls = [int, str, bool, complex, float, set, list, dict, tuple]
    if (type(obj) not in not_allowed_cls):
        obj.name = value
    else:
        raise TypeError("can't add new attribute")
