#!/usr/bin/python3
def safe_print_integer(value):
    """
    función que imprime un entero
    """
    entero = 0
    try:
        entero = int(value)
    except ValueError:
        return False

    print("{}".format(entero))
    return True
