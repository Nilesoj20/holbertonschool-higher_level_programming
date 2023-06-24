#!/usr/bin/python3
""" function that returns the dictionary with simple data structure"""
import json


def class_to_json(obj):
    """converts the given object into a dictionary """
    return obj.__dict__
