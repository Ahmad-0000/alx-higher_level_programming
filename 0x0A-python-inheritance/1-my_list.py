#!/usr/bin/python3
"""
A module containing the solution of the 2nd task.
A class that has "list" as its parent class.
"""


class MyList(list):
    """
    A class that has "list" class as its parent class.

    It also has a public instance attribute to print
    the list in an ascending sorted form
    """

    def print_sorted(self):
        """
        Prints the list after sorting it
        """
        print(sorted(self))
