#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """"
    función que imprime x elementos de una lista
    """
    cont = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            cont += 1
        except Exception:
            break
    print('')
    return cont
