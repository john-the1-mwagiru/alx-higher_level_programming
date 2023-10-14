#!/usr/bin/python3
"""This module defines a class Student """


class Student:
    """Defines class Student"""

    def __init__(self, first_name, last_name, age):
        """Instantiates the class objects"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student"""
        obj_attr = self.__dict__
        if attrs:
            attributes = {a: x[a] for a in x if a in attrs}
            return attributes
        return obj_attr
