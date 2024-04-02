#!/usr/bin/python3
"""
A module containing one function
, "print_square", which is the
solution of the 4th task projct
"""


def print_square(size):
    """
    A function to print a square
    using "#" symbol. size is the
    square's size. size must be an
    integer and must be >= 0, otherwise,
    errors will occur
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for row in range(size):
        for element in range(size):
            print('#', end="")
        print()
