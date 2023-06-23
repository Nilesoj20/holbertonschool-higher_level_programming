#!/usr/bin/python3
""" function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """ writes the json string to a file

    Args:
        my_obj: object
        filename (str): file

    Returns:
        a file
    """
    with open(filename, 'w') as file:
        return json.dump(my_obj, file)
