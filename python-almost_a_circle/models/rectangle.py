#!/usr/bin/python3
""" Rectangle function """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor Rectangle

        Args:
            width (int): rectangle width
            height (int): rectangle height
            x (int): coordinates of the rectangle
            y (int): coordinates of the rectangle
            id (int): rectangle id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ int: private width
        Returns: width
        """
        return self.__width

    @property
    def height(self):
        """ int: private height
        Returns: height
        """
        return self.__height

    @property
    def x(self):
        """ int: private x
        Returns: x
        """
        return self.__x

    @property
    def y(self):
        """ int: private y
        Returns: y
        """
        return self.__y

    @width.setter
    def width(self, value):
        """ Sets value into width, must be int

        Args:
            value (int): width
        """
        self.__width = value

    @height.setter
    def height(self, value):
        """ Sets value into height, must be int

        Args:
            value (int): height
        """
        self.__height = value

    @x.setter
    def x(self, value):
        """ Sets value into x, must be int

        Args:
            value (int): coordinates of the rectangle x
        """
        self.__x = value

    @y.setter
    def y(self, value):
        """ Sets value into y, must be int

        Args:
            value (int): coordinates of the rectangle y
        """
        self.__y = value
