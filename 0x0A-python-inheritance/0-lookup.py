#!/usr/bin/python3
"""
A module containing the solution of the 1st task.
A one function to retrieve all the attributes and
methods of an object in a list format
"""


def lookup(obj):
    """
    A function to retrieve all the methods and attributes
    of an object in a list format.

    "obj" is the object to retrieve its attributes and
    methods.
    """

    return dir(obj)
