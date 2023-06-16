#!/usr/bin/python3
""" class Rectangle that defines a rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """ initialize init
        Args:
            width (int): rectangle width
            height (int): rectangle height"""
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """ Returns: the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets value into height, must be int

        Args:
            value (int): height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets value into width, must be int

        Args:
            value (int): height
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
