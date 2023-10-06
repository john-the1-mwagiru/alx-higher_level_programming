#!/usr/bin/python3
"""This module defines a function that adds 2 integers a,b
a,b are either integers or floats 
"""


def add_integer(a, b=98):
    """Compute and return the sum of two numbers


    Args:
        a(int): A number representing the first addend in the addition.
        b(int): A number representing the second addend in the addition.
    Returns:
        int: A number representing the arithmetic sum of `a` and  `b`.
    """
    if isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
