#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        claves = a_dictionary.values()
        mayor = max(claves)
        for clave, valor in a_dictionary.items():
            if valor == mayor:
                return clave
