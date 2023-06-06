#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    lista_copia = my_list.copy()
    for i in range(0, len(lista_copia)):
        if idx == i:
            lista_copia[i] = element
            return lista_copia
