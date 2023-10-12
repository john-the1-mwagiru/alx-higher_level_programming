#!/usr/bin/python3
"""This module defines an empty class"""


class BaseGeometry:
    """Defines an empty class"""

    def area(self):
        """Public instance method that raises an Exception"""
        Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates the value
        >>> geometry = BaseGeometry()
        >>> geometry.integer_validator("my_int",12)
        >>> geometry.integer_validator("width",89)
        >>> geometry.integer_validator("name","john")
        Traceback (most recent call last):
            ...
        TypeError: name must be an integer
        >>> geometry.integer_validator("age",0)
        Traceback (most recent call last):
            ...
        ValueError: age must be greater than 0
        >>> geometry.integer_validator("distance",-4)
        Traceback (most recent call last):
            ...
        ValueError: distance must be greater than 0

        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
