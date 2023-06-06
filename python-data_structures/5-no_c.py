#!/usr/bin/python3
def no_c(my_string):
    remplazo = ''
    lista = list(my_string)
    for i in range(0, len(lista)):
        if lista[i] == 'c' or lista[i] == 'C':
            lista[i] = remplazo
    texto_nuevo = "".join(lista)
    return texto_nuevo
