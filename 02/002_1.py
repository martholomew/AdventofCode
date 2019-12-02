#!/bin/python
import json

with open("input.json", "r") as f:
    array = json.load(f)

op = 0
while op < len(array):
    if array[op] == 1:
        array[array[op + 3]] = array[array[op + 1]] + array[array[op + 2]]
    elif array[op] == 2:
        array[array[op + 3]] = array[array[op + 1]] * array[array[op + 2]]
    elif array[op] == 99:
        print("Halt!")
        print(array)
        exit()
    else:
        print("ERROR")
        print(array)
        print(array[op])
        exit()
    op += 4
