#!/usr/bin/python3
"""Defines a class Square that inherits from the class Rectangle"""
Rectangle = __import__("rectangle").Rectangle


class Square(Rectangle):
    """Defines a class Square that inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """This is the class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """This function returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """This function sets the values of the square's width and height"""
        self.width = value
        self.height = value

    def __str__(self):
        """This function returns a string representation of the Square instance"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ")" + " "
        string += str(self.x) + "/" + str(self.y) + " " + "-" + " "
        string += str(self.size)
        return string
