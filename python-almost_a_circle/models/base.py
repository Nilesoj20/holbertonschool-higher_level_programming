#!/usr/bin/python3
"""Project base class """
import json


class Base:
    """Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor

        Args:
            id (int): the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ method Serialization

        Args:
            list_dictionaries (dict):  is a list of dictionaries

        Returns:
        the JSON string representation
        """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        else:
            return json.dumps(list_dictionaries)
