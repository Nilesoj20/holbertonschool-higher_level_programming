#!/usr/bin/python3
""" int: class Square that defines a square"""


class Square:
    """ class Square """
    def __init__(self, size=0, position=(0, 0)):
        """ initialize init
        Arg:
             size (int): Private instance attribute
        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

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

    @position.setter
    def position(self, value):
        """ Sets value into position, must be int
        Args:
            value (int): position
        """
        if (not isinstance(value, tuple) or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        int: print in stdout the square with the character #
        Return: print square
        """
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")
        else:
            print("")
