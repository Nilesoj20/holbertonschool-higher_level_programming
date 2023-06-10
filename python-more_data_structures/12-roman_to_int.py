#!/usr/bin/python3
def reglas(lista):
    valor = 0
    if len(lista) == 1:
        return lista.pop()
    for i in range(len(lista)):
        if i != len(lista) - 1 and lista[i] < lista[i+1]:
            valor += lista[i] * -1
        else:
            valor += lista[i]
    return valor


def roman_to_int(roman_string):
    lista = []
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    romano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(0, len(roman_string)):
        if roman_string[i] in romano:
            valor = romano.get(roman_string[i])
            lista.append(valor)
    return reglas(lista)
