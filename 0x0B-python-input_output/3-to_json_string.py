#!/usr/bin/python3
import json

"""This module SON representation of an object (string)"""


def to_json_string(my_obj):
    """This function returns the JSON representation of an object(string)
    Args:
     my_obj(any):object being passed in

    Returns:
        json object

    """
    new_object = json.dumps(my_obj)
    return new_object
