#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list = list(reversed(my_list))
    for i in range(0, len(my_list)):
        print("{}".format(my_list[i]))
