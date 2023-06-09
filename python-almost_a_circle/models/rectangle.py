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

    @width.setter
    def width(self, value):
        """ Sets value into width, must be int

        Args:
            value (int): width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ int: private height
        Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets value into height, must be int

        Args:
            value (int): height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ int: private x
        Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets value into x, must be int

        Args:
            value (int): coordinates of the rectangle x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ int: private y
        Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets value into y, must be int

        Args:
            value (int): coordinates of the rectangle y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the rectangle area """
        return (self.width * self.height)

    def display(self):
        """print a rectangle with #"""
        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for j in range(self.width)]
            print()

    def __str__(self):
        """ method __str__ that returns a message"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ Method assigns an argument to each attribute

        Args:
            *args (tuple):
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
        """
        if args and len(args) != 0:
            flag = 1
            for arg in args:
                if flag == 1:
                    self.id = arg
                    flag += 1
                    continue
                if flag == 2:
                    self.width = arg
                    flag += 1
                    continue
                if flag == 3:
                    self.height = arg
                    flag += 1
                    continue
                if flag == 4:
                    self.x = arg
                    flag += 1
                    continue
                if flag == 5:
                    self.y = arg
                    flag += 1
                    continue

        if kwargs and len(kwargs) != 0:
            for clave, valor in kwargs.items():
                if clave == "id":
                    self.id = valor
                    continue
                if clave == "width":
                    self.width = valor
                    continue
                if clave == "height":
                    self.height = valor
                    continue
                if clave == "x":
                    self.x = valor
                    continue
                if clave == "y":
                    self.y = valor
                    continue

    def to_dictionary(self):
        """method the dictionary representation of a Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height,
                'width': self.width}
