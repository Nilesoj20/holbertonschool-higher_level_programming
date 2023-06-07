#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    size = len(my_list)
    lista = []
    for i in range(size):
        if my_list[i] % 2 == 0:
            lista.append(True)
        else:
            lista.append(False)
    return lista
