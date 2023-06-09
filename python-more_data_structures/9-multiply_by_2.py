#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    orden = sorted(a_dictionary.items())
    tmp = {}
    for clave, valor in orden:
        x = valor * 2
        tmp[clave] = x
    return tmp
