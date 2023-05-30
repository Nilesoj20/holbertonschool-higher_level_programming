#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            flag = 32
        else:
            flag = 0
        print("{:c}".format(ord(str[i]) - flag), end="")
    print()
