#!/usr/bin/python3
"""Function that reads a text file"""


def read_file(filename=""):
    """ function to read a file
    Args:
        filename (str): a file.txt

    Return:
        prints it to stdout"""
    with open(filename, 'r') as file:
        print(file.read(), end="")
