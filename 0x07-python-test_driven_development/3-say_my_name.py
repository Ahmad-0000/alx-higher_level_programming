#!/usr/bin/python3
""" A module contains a function -
(say_my_name) - to print the first
and last name of a person. first_name
and last_name must both be strings,
otherwise a TypeError will be raised
with the sentence "first_name must be a string" or
"last name must be a string"
"""


def say_my_name(first_name, last_name=""):
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print(f"My name is {first_name} {last_name}")
