#!/usr/bin/python3
"""This module  returns True if the object is an instance of otherwise False"""


def inherits_from(obj, a_class):
    """This function returns True if the object is an instance of the class otherwise returns False
    Args:
        obj(any): Object to check
        a_class(type): The class to match the type of obj to.

    Returns:
       if obj is exactly an instance of a_class  - True
        otherwise - False
    """
    return type(obj) is a_class
