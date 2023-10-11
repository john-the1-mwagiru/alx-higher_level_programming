#!/usr/bin/python3
"""This module tests if an object is an instance of the specified class"""


def is_same_class(obj, a_class):
    """This method returns True if the object is exactly an instance of the specified class otherwise False
    Args:
        obj(any): The object to check
        a_class(type): The class to match the type of obj to.
    Returns:
        if obj is exactly an instance of a_class  - True
        otherwise - False
    """
    if type(obj) == a_class:
        return True
    return False
