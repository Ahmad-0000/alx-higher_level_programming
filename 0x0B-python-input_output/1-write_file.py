#!/usr/bin/python3
"""
A module containing one function:
    "write_file"
"""


def write_file(filename="", text=""):
    """
    A function to write into a file provided in the path "filename"
    . If "filename" is not provided, the default is "". if "filename"
    does not exist, it will be created. "text" is the text to be
    written into the file, if "text" is not provided, the default is
    "".

    "filename" will be opened with encoding set to "utf-8"

    Return value: is the number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as my_file:
        return my_file.write(text)
