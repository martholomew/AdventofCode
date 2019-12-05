#!/bin/python
import json

with open("input.json", "r") as f:
    array = json.load(f)

op = 0
while op < len(array):
    if array[op] == 3:
        array[array[op + 1]] = 5
        op += 2

    elif array[op] == 99:
        print("Halt!")
        print(array)
        exit()

    else:
        modes = str(array[op]).rjust(4, '0')[:2]
        if modes[1] == "1":
            num = array[op + 1]
        elif modes[1] == "0":
            num = array[array[op + 1]]
        else:
            print("no good")
            exit()
        if modes[0] == "1":
            num_2 = array[op + 2]
        elif modes[0] == "0":
            num_2 = array[array[op + 2]]
        else:
            print("no good")
            exit()
        if str(array[op])[-1] == "1":
            array[array[op + 3]] = num + num_2
        elif str(array[op])[-1] == "2":
            array[array[op + 3]] = num * num_2
        elif str(array[op])[-1] == "4":
            print("Output:")
            print(num)
            op += 2
            continue
        elif str(array[op])[-1] == "5":
            if num:
                op = num_2
                continue
            else:
                op += 3
                continue
        elif str(array[op])[-1] == "6":
            if not num:
                op = num_2
                continue
            else:
                op += 3
                continue
        elif str(array[op])[-1] == "7":
            if num < num_2:
                array[array[op + 3]] = 1
            else:
                array[array[op + 3]] = 0
        elif str(array[op])[-1] == "8":
            if num == num_2:
                array[array[op + 3]] = 1
            else:
                array[array[op + 3]] = 0
        else:
            print("ERROR")
            print(array)
            print(array[op])
            exit()
        op += 4
