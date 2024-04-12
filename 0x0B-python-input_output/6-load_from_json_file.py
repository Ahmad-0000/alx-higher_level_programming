#!/usr/bin/python3
"""
A module containing one function:
    "load_from_json_file"
"""
import json
import os


def load_from_json_file(filename):
    """
    A function to convert a JSON string provided in
    "filename" to a Python object.
    """

    if os.path.isfile(filename):
        with open(filename, encoding="utf-8") as my_file:
            content = my_file.read()
            if content:
                return json.loads(content)
            else:
                return
    return
