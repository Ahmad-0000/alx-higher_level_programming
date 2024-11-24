#!/usr/bin/python3
"""
4th task's solution
"""

def is_kind_of_class(obj, a_class):
    """Returns true if 'obj' is an instance of 'a_class' or
    of a superclass of 'a_class'
    """
    return isinstance(obj, a_class)
