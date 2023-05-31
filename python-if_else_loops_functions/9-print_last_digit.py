#!/usr/bin/python3
def print_last_digit(number):
    rest = abs(number) % 10
    rest *= -1 if number < 0 else 1
    if rest < 0:
        print(rest * -1, end="")
        return rest * -1
    if rest == 0 or rest > 0:
        print(rest, end="")
        return rest
