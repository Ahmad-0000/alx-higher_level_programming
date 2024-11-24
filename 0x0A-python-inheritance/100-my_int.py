#!/usr/bin/python3
"""
A modlue containg one class:
    "MyInt"
"""


class MyInt(int):
    """
    A customized version of the "int" class
    """

    def __init__(self, value):
        """
        Initialization function
        """

        self.value = value

    def __eq__(self, value):
        """
        Modified "==" to do the job of "!="
        """
        return not self.value == value

    def __ne__(self, value):
        """
        Modified "!=" to do the job of "=="
        """
        return not self.value != value
