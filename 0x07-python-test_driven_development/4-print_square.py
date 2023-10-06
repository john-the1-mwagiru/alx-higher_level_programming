#!/usr/bin/python3
"""Defines a function that prints a square with the character #"""


def print_square(size):
    """This function takes in a the size paremeter and returns
    a square with an equal height and an equal width.

    Args:
        size: A number representing the width and height of the square.
    Returns:
        A square represented with the character #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            j = "#"
            print(j, end="")
        print()
