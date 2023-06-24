#!/usr/bin/python3
""" function that returns the dictionary with simple data structure
"""


def class_to_json(obj):
    """converts the given object into a dictionary

    Args:
        obj (class): object

    Returns:
        a dictionary class object
    """
    return obj.__dict__
