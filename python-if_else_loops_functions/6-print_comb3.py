#!/usr/bin/python3
for i in range(0, 10):
    for x in range(i + 1, 10):
        if i == 8:
            print("{:d}{:d}".format(i, x))
        else:
            print("{:d}{:d}, ".format(i, x), end="")
