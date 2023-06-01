#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    ar = sys.argv
    if len(ar) == 1:
        print("0 arguments.")
    elif len(ar) == 2:
        print("1 argument:")
    elif len(ar) > 2:
        print("{} arguments:".format(len(ar)-1))
    for i in range(1, len(ar)):
        print("{}: {}".format(i, ar[i]))
