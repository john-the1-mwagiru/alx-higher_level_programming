#!/usr/bin/python3
"""Defines a function that returns the dictionary description"""


def class_to_json(obj):
    """This function returns the dictionary description with simple data structure
    Args:
        obj(any): python data structure

    """
    return obj.__dict__
