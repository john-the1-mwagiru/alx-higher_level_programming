#!/usr/bin/python3

"""This module SON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """This function returns the JSON representation of an object(string)
    Args:
     my_obj(any):object being passed in

    Returns:
        json object

    """
    return json.dumps(my_obj)
