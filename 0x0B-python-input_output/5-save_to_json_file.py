#!/usr/bin/python3
"""This module writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """This  function writes an Object to a text file, using a JSON representation
    Args:
        my_obj(any):python object passed into the function
        filename: name of our file
    """
    with open(filename, "w", encoding="utf-8") as filename:
        new_file = json.dumps(my_obj)
        filename.write(new_file)
