#!/bin/python
import json

with open("input.json", "r") as f:
    array_orig = json.load(f)

output = 0
for noun in range(100):
    for verb in range(100):
        array = [dum for dum in array_orig]
        array[1] = noun
        array[2] = verb
        op = 0
        inst = 0
        while inst != 99:
            inst = array[op]
            if inst == 1:
                array[array[op + 3]] = array[array[op + 1]] + array[array[op + 2]]
            elif inst == 2:
                array[array[op + 3]] = array[array[op + 1]] * array[array[op + 2]]
            elif inst == 99:
                output = array[0]
                if output == 19690720:
                    print(noun)
                    print(verb)
            else:
                print("ERROR")
                print(array)
                print(array[op])
                exit()
            op += 4
