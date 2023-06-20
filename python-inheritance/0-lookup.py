#!/usr/bin/python3
"""Function that returns a list with attributes and methods"""


def lookup(obj):
    """ method that uses the dir() method to return
        the methods and attributes of the given object

    Args:
        obj (class): object to be checked

    Returns:
        the methods and attributes that the object has
    """
    return dir(obj)
