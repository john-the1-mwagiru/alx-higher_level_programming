#!/usr/bin/python3
"""This module defines a function that prints a person's first name 
and a person's lastname






Args:
    first_name: A string that represents a persons first name
    last_name: A string that represents a persons last name
Raises:
    TypeError: If the first_name is not a string .
    TypeError: If the last-name is not a string .
Returns:
    A new string representing a person's full name.
    """


def say_my_name(first_name, last_name=""):
    """This function takes in a person's firstname and last name and returns them in a sentence"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    return f"My name is {first_name} {last_name}"
