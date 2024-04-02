#!/usr/bin/python3
"""
A module containing one function
"text_indentation", which the
solution of the 6th task project
"""


def text_indentation(text):
    """
    A function to write a text.
    If text contains "?", "." or
    ":" 2 lines after each of
    these symbols will be printed.
    text must be an integer, otherwise
    an error will occure
    """

    if type(text) is not str:
        raise TypeError('text must be a string')
    line_beginning = 1
    for char in text:
        if ord(char) == ord(' ') and line_beginning == 1:
            pass
        elif ord(char) == ord('.') or ord(char) == ord('?') \
                or ord(char) == ord(':'):
            line_beginning = 1
            print(char + '\n\n', end="")
        elif ord(char) != ord(' ') and line_beginning == 1:
            print(char, end="")
            line_beginning = 0
        else:
            print(char, end="")
