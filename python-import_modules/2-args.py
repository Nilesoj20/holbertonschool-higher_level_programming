#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    ar = sys.argv
    if len(ar) == 1:
        print("0 arguments.")
    print("{} argument:".format(len(ar)-1))
    for i in range(1, len(ar)):
        print("{}: {}".format(i, ar[i]))
