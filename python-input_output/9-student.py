#!/usr/bin/python3
""" class to define students """


class Student:
    """ base class student pass"""
    def __init__(self, first_name, last_name, age):
        """ init method with 2 parameters

        Args:
            first_name (str): student's name
            last_name (str): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ that retrieves a dictionary representation of a Student
        """
        return self.__dict__
