#!/usr/bin/python3
"""Checks if the object is exactly an instance of the specified class """


def is_same_class(obj, a_class):
    """validates if obj is of type a_class

    Args:
        obj (chr): object to be compared
        a_class (str): class to be compared

    Returns:
        True if it is an instance of the class otherwise it returns False
    """
    return type(obj) == a_class
