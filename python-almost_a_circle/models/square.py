#!/usr/bin/python3
"""New class square inheriting from rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class that creates a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor Rectangle

        Args:
            width (int): rectangle width
            height (int): rectangle height
            x (int): coordinates of the rectangle
            y (int): coordinates of the rectangle
            id (int): rectangle id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ int: private size
        Returns: size
        """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets value into size
        Args:
            value (int): width or height
        """
        self.width = value
        self.height = value

    def __str__(self):
        """modify the __str__ method """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

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
                    self.height = arg
                    flag += 1
                    continue
                if flag == 3:
                    self.x = arg
                    flag += 1
                    continue
                if flag == 4:
                    self.y = arg
                    flag += 1
                    continue

        if kwargs and len(kwargs) != 0:
            for clave, valor in kwargs.items():
                if clave == "id":
                    self.id = valor
                    continue
                if clave == "size":
                    self.width = valor
                    self.height = valor
                    continue
                if clave == "x":
                    self.x = valor
                    continue
                if clave == "y":
                    self.y = valor
                    continue

    def to_dictionary(self):
        """method the dictionary representation of a square"""
        return {'id': self.id, 'x': self.x,
                'size': self.size, 'y': self.y}
