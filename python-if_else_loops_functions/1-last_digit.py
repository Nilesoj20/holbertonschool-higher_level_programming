#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
re = abs(number) % 10
re *= -1 if number < 0 else 1

if re > 5:
    print(f"Last digit of {number} is {re} and is greater than 5")
elif re == 0:
    print(f"Last digit of {number} is {re} and is 0")
else:
    print(f"Last digit of {number} is {re} and is less than 6 and not 0")
