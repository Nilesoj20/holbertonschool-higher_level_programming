#!/usr/bin/python3
""" Function that checks if it is an instance that I inherit or not"""


def inherits_from(obj, a_class):
    """ Checks is a instance that  inherit

    Args:
        obj (chr)
        a_class (str): class to be compared

    Returns:
        True if it is an instance otherwise it returns False
    """

    if a_class != bool:
        return isinstance(obj, a_class)
    else:
        return False
