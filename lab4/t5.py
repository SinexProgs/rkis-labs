import json
import random

try:
    print((random.randint(0, 2) / random.randint(0, 2)))
except ZeroDivisionError:
    print("Division by zero has occurred!")

try:
    print(open("hello.txt").readline())
except FileNotFoundError:
    print("Couldn't find file!")

try:
    print(json.load(open("t5.py")))
except json.JSONDecodeError:
    print("Couldn't parse JSON!")