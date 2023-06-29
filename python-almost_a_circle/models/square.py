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
