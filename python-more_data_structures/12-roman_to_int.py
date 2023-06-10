#!/usr/bin/python3
def reglas(lista):
    if len(lista) == 1:
        return lista.pop()

    if lista[0] < lista[1]:
        valor = lista[0] - lista[1]
        for i in range(2, len(lista)):
            valor = valor + lista[i]
    else:
        valor = sum(lista)
    if valor < 0:
        valor *= -1
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
