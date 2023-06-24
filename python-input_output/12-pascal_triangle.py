#!/usr/bin/python3
"""function that represents the Pascal's Triangle"""


def pascal_triangle(n):
    """devuelve una lista de listas de enteros
    que representan el triángulo de Pascal de n

    Args:
        n (int): size number
    Returns:
        a list of lists of integers representing the triangle
    """
    if n <= 0:
        return []

    triangulo = [[1]]
    while len(triangulo) != n:
        tr = triangulo[-1]
        tmp = [1]
        for i in range(len(tr) - 1):
            tmp.append(tr[i] + tr[i + 1])
        tmp.append(1)
        triangulo.append(tmp)
    return triangulo
