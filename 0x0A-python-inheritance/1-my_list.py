#!/usr/bin/python3
"""This module defines a class that inherits from another class"""


class MyList(list):
    """This class defines a class that prints a list but in ascending order"""

    def print_sorted(self):
        if isinstance(self, list):
            self.sort()
            print(self)
