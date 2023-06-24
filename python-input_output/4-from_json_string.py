#!/usr/bin/python3
"""function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """ function that changes to a python object

    Args:
        my_str (str): string to convert

    Returns:
        (Python data structure) represented by a JSON string
    """
    return (json.loads(my_str))