#!/usr/bin/python3
def search_replace(my_list, search, replace):
    tmp = my_list.copy()
    for i in range(len(my_list)):
        if search == my_list[i]:
            tmp[i] = replace
    return tmp
