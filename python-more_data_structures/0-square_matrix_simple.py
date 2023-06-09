#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    temp = []
    cuadrado = lambda elemento: elemento ** 2
    temp = list(map(lambda fila: list(map(cuadrado, fila)), matrix))
    return temp
