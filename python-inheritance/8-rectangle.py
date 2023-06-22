#!/usr/bin/python3
""" an empty class BaseGeometry """


class BaseGeometry:
    """ Function that raises an error message """

    def area(self):
        """Public instance method that raises an error message """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that is in charge of validating the received value

        Args:
            name (str): name
            value (int): value to be evaluated

        Return:
            error messages for each case
        """

        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Creates a Rectangle class with height and width """

    def __init__(self, width, height):
        """ init constructor method """

        self.__width = width
        self.__height = height
        if type(height) != int:
            super().integer_validator("height", self.__height)
        if type(width) != int:
            super().integer_validator("width", self.__width)
