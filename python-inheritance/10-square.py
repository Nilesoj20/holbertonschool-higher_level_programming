#!/usr/bin/python3
"""Import parent classes from the file 9-rectangle.py """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a Square class receiving size """

    def __init__(self, size):
        """ Init constructor method

        Args:
            size (int): attribute that receives the method

        Return:
            the area and the message
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
