#!/usr/bin/python3
"""
A module containing one function:
    "load_from_json_file"
"""
import json


def load_from_json_file(filename):
    """
    A function to convert a JSON string provided in
    "filename" to an object.
    """

    with open(filename, encoding="utf-8") as my_file:
        obj = json.load(my_file)
    return obj
