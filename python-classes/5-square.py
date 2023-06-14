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
    def size(self):
        """ int: private size
        Returns: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets value into size, must be int

        Args:
            value (int): size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        int: print in stdout the square with the character #
        Return: print square
        """
        if self.__size != 0:
            for i in range(self.__size):
                for x in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
