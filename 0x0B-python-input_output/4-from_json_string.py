#!/usr/bin/python3
"""This module returns a Python data structure from JSON"""
import json


def from_json_string(my_str):
    """This function returns an object (Python data structure) represented by a JSON string
    Args:
        my_str(str): json representation which is a string
    Returns:
        a python object
    """
    return json.loads(my_str)
