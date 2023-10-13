#!/usr/bin/python3
"""This module reads a text file and prints it out"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as filename:
        new_file = filename.read()
        print(new_file)
