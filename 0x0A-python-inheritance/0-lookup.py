#!/usr/bin/python3
"""This module  returns the list of available attributes and methods of an object"""


def lookup(obj):
    """This method returns a list of available attributes and methods of an object"""
    return dir(obj)
