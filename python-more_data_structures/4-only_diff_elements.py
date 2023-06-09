#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    no_comun = set_1.symmetric_difference(set_2)
    return no_comun
