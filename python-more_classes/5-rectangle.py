#!/usr/bin/python3
""" class Rectangle that defines a rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """ initialize init
        Args:
            width (int): rectangle width
            height (int): rectangle height"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """ returns the value of width"""
        return self.__width

    @property
    def height(self):
        """ Returns: the value of height"""
        return self.__height

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
        self.__width = value

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
        self.__height = value

    def area(self):
        """ returns the rectangle area """
        return (self.__width * self.__height)

    def perimeter(self):
        """  returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """  returns rectangle with the character # """
        if self.__width == 0 or self.__height == 0:
            return ""
        res = []
        for i in range(self.__height):
            for x in range(self.__width):
                res.append("#")
            if i != self.__height - 1:
                res.append("\n")
        return ("".join(res))

    def __repr__(self):
        """  returns rectangle with the character # """
        string = "Rectangle(" + str(self.__width)
        string = string + ", " + str(self.__height) + ")"
        return (string)

    def __del__(self):
        """ an instance of Rectangle is deleted """
        print("Bye rectangle...")
