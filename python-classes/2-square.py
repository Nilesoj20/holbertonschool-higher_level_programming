#!/usr/bin/python3
""" int: class Square that defines a square
"""


class Square:
    """ class Square """
    def __init__(self, size=0):
        """ initialize init
        Arg:
            size (int): Private instance attribute
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
