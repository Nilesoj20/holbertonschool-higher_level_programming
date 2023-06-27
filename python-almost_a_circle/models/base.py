#!/usr/bin/python3
"""Project base class """


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
