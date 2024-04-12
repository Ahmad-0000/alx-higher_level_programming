#!/usr/bin/python3
"""
A module containing one function:
    "read_file"
"""


def read_file(filename=""):
    """
    A function to read a file provided in the path "filename"
    and to print its output in the stdout. If "filename" is
    not provided, the default is "". "filename" must be a path
    to an existing "file".

    "filename" will be opened with encoding set to "utf-8"
    """

    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
