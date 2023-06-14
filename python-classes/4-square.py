#!/usr/bin/python3
""" int: class Square that defines a square"""


class Square:
    """ class Square """
    def __init__(self, size=0):
        """ initialize init
        Arg:
             size (int): Private instance attribute
        """
        self.__size = size

    def area(self):
        """ int: area method
         Returns: area
        """
        return self.__size * self.__size

    @property
    """ int: private size

    Returns: size
    """
    def size(self):
        return self.__size

    @size.setter
    """
    Sets value into size, must be int

    Args: 
        value (int): size
    """
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
