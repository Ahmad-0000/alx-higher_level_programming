#!/usr/bin/python3
"""
A module containing one class:
    "BaseGeometry"
Thie is class will be expanded
later.
"""


class BaseGeometry():
    """
    An empty class to be filled later
    in the subsequent tasks
    """

    def area(self):
        """
        A method to raise this exception:
            "Exception: area() is not implemented"
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A value to check that "value" is an integer
        and is greater that 0
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
