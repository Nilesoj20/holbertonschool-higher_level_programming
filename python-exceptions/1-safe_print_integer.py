#!/usr/bin/python3
def safe_print_integer(value):
    """
    función que imprime un entero
    """
    try:
        print("{:d}".format(value))
    except ValueError:
        return False

    return True
