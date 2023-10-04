#!/usr/bin/python3

"""This module defines a class Rectangle , with a width that is a private instance attrributes
    and a height as a private instance attribute
"""


class Rectangle:
    """This class defines a rectangle with two attributes; height and width"""

    def __init__(self, width=0, height=0):
        """This method instantiates our objects
        Args:
        width (int): The width of the new rectangle.
        height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This method retrives the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """This method sets the width attribute value"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """This method returns the height attribute of our object"""
        return self.__height

    @height.setter
    def height(self, height):
        """This method sets the height attribute value"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """This method calculates the rectangle's area"""
        return self.__height * self.__width

    def perimeter(self):
        """This method calculates the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """Return an informal and nicely printable string representation of an instance

        Represents a rectangle with the # character
        """
        if self.__height == 0 or self.__width == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Returns a formal string representation of the object instance"""
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
