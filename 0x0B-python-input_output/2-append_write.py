#!/usr/bin/python3
"""
A module containing one function:
    "append_write"
"""


def write_file(filename="", text=""):
    """
    A function to append into a file provided in the path "filename"
    . If "filename" is not provided, the default is "". if "filename"
    does not exist, it will be created. "text" is the text to be
    appended into the file, if "text" is not provided, the default is
    "".

    "filename" will be opened with encoding set to "utf-8"

    Return value: is the number of characters appended
    """

    with open(filename, 'a', encoding="utf-8") as my_file:
        return my_file.write(text)
