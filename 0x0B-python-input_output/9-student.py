#!/usr/bin/python3
"""
A module containing one class:
    "Student"
"""


class Student:
    """
    A class that initialize an instance with public
    instance attributes "first_name", "last_name"
    and "age". Also the object will have access to
    a public method "to_json"
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializing method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        A method to retrive the "Studend" class instance dictionary
        description
        """
        return self.__dict__
