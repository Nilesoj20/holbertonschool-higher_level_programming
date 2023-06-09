#!/usr/bin/python3
def cuadrado(elemento):
    return elemento ** 2


def square_matrix_simple(matrix=[]):
    temp = []
    temp = list(map(lambda fila: list(map(cuadrado, fila)), matrix))
    return temp
