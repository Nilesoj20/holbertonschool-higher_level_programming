#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    for i in range(0, len(my_list)):
        if idx == i:
            my_list[i] = element
            return my_list
