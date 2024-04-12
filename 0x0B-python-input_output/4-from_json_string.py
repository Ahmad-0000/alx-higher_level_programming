#!/usr/bin/python3
"""
A module containing one function:
    "from_json_string"
"""
import json


def from_json_string(my_str):
    """
    A function to convert a JSON string "my_str" to a Python
    object.
    """

    return json.loads(my_str)
