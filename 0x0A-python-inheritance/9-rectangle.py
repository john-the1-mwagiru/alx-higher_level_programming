#!/usr/bin/python3
"""This module defines an empty class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """This function instantiates our objects and also validates the type of our objects
        Args:
            width(int): width of our rectangle
            height(int): height of our rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

    def area(self):
        return self.__height * self.__width
