#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        my_list.reverse()
        for i in range(0, len(my_list)):
            print("{:d}".format(my_list[i]))
