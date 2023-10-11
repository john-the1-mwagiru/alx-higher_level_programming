#!/usr/bin/python3
"""This module defines a class that inherits from another class"""


class MyList(list):
    """This class defines a class that prints a list but in ascending order"""

    def print_sorted(self):
        """Print a list in sorted ascending order"""
        print(sorted(self))
