#!/usr/bin/python3

"""This module defines a class Rectangle , with a width that is a private instance attrributes
    and a height as a private instance attribute
"""


class Rectangle:
    """This class defines a rectangle with two attributes; height and width"""

    def __init__(self, width=0, height=0):
        """This method instantiates our objects"""
        self.__width = width
        self.__height = height

    def set_width(self, width):
        """This method sets the width attribute value"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    def get_width(self):
        """This method retrives the width"""
        return self.__width

    def set_height(self, height):
        """This method sets the height attribute value"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def get_height(self):
        """This method returns the height attribute of our object"""
        return self.__height

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"


x = Rectangle()
x.set_height(2)
x.set_width(3)
fetch = x.get_height()
fetch1 = x.get_width()
print(x)
