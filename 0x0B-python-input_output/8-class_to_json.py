#!/usr/bin/python3
"""
A module containing one function:
    "class_to_json"
"""
import json


def class_to_json(obj):
    """
    A function to return the dictionary description of
    an object "obj" to be converted into a string in
    JSON format

    Return value: is the dictionary description of the
    "obj"
    """

    return (obj.__dict__)
