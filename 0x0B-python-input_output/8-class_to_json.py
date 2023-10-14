#!/usr/bin/python3
"""Defines a function that returns the dictionary description"""

import json


def class_to_json(obj):
    """This function returns the dictionary description with simple data structure
    Args:
        obj(any): python data structure

    """
    json_string = json.dumps([ob.__dict__ for ob in obj])
    return json_string
