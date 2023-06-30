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
            return "[]"
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
        if list_objs is None:
            with open(f"{cls.__name__}.json", 'w') as file:
                file.write(cls.to_json_string([]))
        else:
            with open(f"{cls.__name__}.json", 'w') as file:
                lista = [r.to_dictionary() for r in list_objs]
                json_dic = cls.to_json_string(lista)
                file.write(json_dic)

    @staticmethod
    def from_json_string(json_string):
        """  the static method deserialization

        Args:
            json_string (): a list of dictionaries

        Returns:
            the list of the JSON string
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance with all attributes already set

        Args:
            **dictionary (dict): a double pointer to a dictionary
        Returns:
             returns an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """classes instantiated from a file of JSON strings.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as file:
                lista = cls.from_json_string(file.read())
                return [cls.create(**d) for d in lista]
        except IOError:
            return []
