#!/usr/bin/python3
"""
A module containing one function:
    "save_to_json_file"
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function to write an object "my_obj"
    into a file "filename" using JSON foramt.
    """

    with open(filename, 'w', encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
