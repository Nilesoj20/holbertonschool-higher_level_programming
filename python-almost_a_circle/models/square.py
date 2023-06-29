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
