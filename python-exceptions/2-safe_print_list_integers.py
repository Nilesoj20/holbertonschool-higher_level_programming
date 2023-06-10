#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    imprime primeros x elementos de una lista y solo números enteros
    """
    cont = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            pass
        else:
            cont += 1
    print()
    return cont
