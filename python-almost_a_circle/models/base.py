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

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string representation
        Args:
            list_objs (list): list of instances who inherits of Base
        Returns:
            string representation of list_objs to a file
        """
        nombre = cls.__name__
        nombre_archivo = f"{nombre}.json"
        with open(nombre_archivo, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                lista = [r.to_dictionary() for r in list_objs]
                json_dic = cls.to_json_string(lista)
                file.write(json_dic)
