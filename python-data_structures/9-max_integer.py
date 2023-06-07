#!/usr/bin/python3
def max_integer(my_list=[]):
    size_len = len(my_list)
    if size_len == 0:
        return None
    my_list.sort(reverse=True)
    return my_list[0]
