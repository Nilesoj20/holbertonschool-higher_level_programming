#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            if x == 2:
                print("{:d}".format(matrix[i][x]), end="")
            else:
                print("{:d} ".format(matrix[i][x]), end="")
        print()
