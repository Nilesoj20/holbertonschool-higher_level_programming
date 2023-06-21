#!/usr/bin/python3
""" Check if the object is an instance
or is an class that inherited the specified class"""


def is_kind_of_class(obj, a_class):
    """ checks whether it is an object of a specific class

    Args:
        obj (chr): object to be compared
        a_class (str): class to be compared

    Returns:
            True if it is an instance otherwise it returns False
    """
    return isinstance(obj, a_class)
