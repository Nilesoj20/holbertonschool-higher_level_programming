#!/usr/bin/python3
"""Function that writes a string to a text file """


def write_file(filename="", text=""):
    """  a function that writes a string to a text file

    Args:
        filename (str): a file.txt
        text (str): text to be added

    Return:
        number of characters
    """

    with open(filename, 'w') as file:
        file.write(text)
        return len(text)
