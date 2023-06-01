#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ar = sys.argv
    suma = 0
    if len(ar) == 1:
        print("0")
        exit()
    for i in range(1, len(ar)):
        x = int(ar[i])
        suma += x
    print(suma)
