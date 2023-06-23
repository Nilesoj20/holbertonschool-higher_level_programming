#!/usr/bin/python3
"""function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """function that adds to the end of the file

    Args:
        filename (str): a file.txt
        text (str): text to be added

    Return:
        number of characters
    """

    with open(filename, 'a') as file:
        file.write(text)
        return len(text)
