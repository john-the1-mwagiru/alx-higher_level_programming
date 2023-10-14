#!/usr/bin/python3

"""This module defines a function that creates an object from a json file"""
import json


def load_from_json_file(filename):
    """This function creates an object from a json file"""
    with open(filename, "r", encoding="utf-8") as filename:
        load_from = filename.read()
        print(json.loads(load_from))
