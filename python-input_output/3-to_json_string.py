#!/usr/bin/python3
""" function that converts an object into a json
    representation (string)"""
import json


def to_json_string(my_obj):
    """converts an object to a json representation (string)

    Returns:
        json representation (string)
    """

    string_json = json.dumps(my_obj)
    return string_json
