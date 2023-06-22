#!/usr/bin/python3
"""Import parent classes from the file 9-rectangle.py """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a Square class receiving size """

    def __init__(self, size):
        """ Init constructor method """

        self.__size = size

    def area(self):
        """ Change to the area method to return area"""

        return self.__size * self.__size

    def __str__(self):
        """ method for printing description """

        return "[Rectangle] {}/{}".format(self.__size, self.__size)
