#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    llave = a_dictionary.keys()
    orden = sorted(a_dictionary.items())
    for clave, valor in orden:
        print(f"{clave}: {valor}")
