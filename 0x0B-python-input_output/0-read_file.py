#!/usr/bin/python3
"""This module reads a text file and prints it out"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename: file that will acts as our input
    Returns:
        file details to our stdout

    """
    with open(filename, "r", encoding="utf-8") as filename:
        new_file = filename.read()
        print(new_file)
