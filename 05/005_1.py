#!/bin/python
import json

with open("input.json", "r") as f:
    array = json.load(f)

op = 0
while op < len(array):
    if array[op] == 1:
        array[array[op + 3]] = array[array[op + 1]] + array[array[op + 2]]
        op += 4
    elif array[op] == 2:
        array[array[op + 3]] = array[array[op + 1]] * array[array[op + 2]]
        op += 4
    elif array[op] == 3:
        print("input")
        array[array[op + 1]] = 1
        op += 2
    elif array[op] == 4:
        print("output")
        print(array[array[op + 1]])
        op += 2
    elif len(str(array[op])) > 2:
        if str(array[op])[-1] == "4":
            op += 2
            continue
        if len(str(array[op])) == 3:
            modes = "0" + str(array[op])[0]
        else:
            modes = str(array[op])[:2]
        if modes[1] == "1":
            num = array[op + 1]
        else:
            num = array[array[op + 1]]
        if modes[0] == "1":
            num_2 = array[op + 2]
        else:
            num_2 = array[array[op + 2]]
        if str(array[op])[-1] == "1":
            array[array[op + 3]] = num + num_2
        elif str(array[op])[-1] == "2":
            array[array[op + 3]] = num * num_2
        op += 4

    elif array[op] == 99:
        print("Halt!")
        print(array)
        exit()
    else:
        print("ERROR")
        print(array)
        print(array[op])
        exit()
