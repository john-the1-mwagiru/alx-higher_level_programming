#!/usr/bin/python3
"""This module defines an empty class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle:
    def __init__(self, width, height):
        """This function instantiates our objects and also validates the type of our objects
        Args:
            width(int): width of our rectangle
            height(int): height of our rectangle
        """
        BaseGeometry.integer_validator(self, name="width", value=width)
        self.__width = width
        BaseGeometry.integer_validator(self, name="height", value=height)
        self.__height = height
