#!/usr/bin/python3
""" A modult containing one function
"say_my_name". It's the solution
of the third task of the project
"0x07-python-test_driven_development"
"""


def say_my_name(first_name, last_name=""):
    """
    A function to print "My name is <
    first name> <last name>", where <first
    name> and <last name> are strings,
    otherwise, errors will occur
    """

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print(f"My name is {first_name} {last_name}")
