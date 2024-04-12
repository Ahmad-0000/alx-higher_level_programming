#!/usr/bin/python3
"""
A module containing one function:
    "to_json_string"
"""
import json


def to_json_string(my_obj):
    """
    A function to convert a Python object "my_obj" to JSON
    string.
    """

    return json.dumps(my_obj)
