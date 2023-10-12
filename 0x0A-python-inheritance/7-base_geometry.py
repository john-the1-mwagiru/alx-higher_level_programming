#!/usr/bin/python3
"""This module defines an empty class"""


class BaseGeometry:
    """Defines an empty class"""

    def area(self):
        """Public instance method that raises an Exception"""
        Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates the value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
