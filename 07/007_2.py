#!/bin/python

from itertools import permutations

with open("input.txt") as f:
    input_array = [int(num) for num in f.read().rstrip().split(',')]


def run_comp(array, input_num, phase_num, op):
    while op < len(array):
        if array[op] == 3:
            if op == 0:
                array[array[op + 1]] = phase_num
            else:
                array[array[op + 1]] = input_num
            op += 2

        elif array[op] == 99:
            return(False, False, False)

        else:
            modes = str(array[op]).rjust(4, '0')[:2]
            if modes[1] == "1":
                num = array[op + 1]
            elif modes[1] == "0":
                num = array[array[op + 1]]
            else:
                print("no good")
                exit()
            if str(array[op])[-1] == "4":
                return(array[array[op + 1]], array, op + 2)
                continue
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

solutions = []
for perm in permutations([5,6,7,8,9]):
    input_num = 0
    save_op = [0, 0, 0, 0, 0]
    save_array = [input_array[:], input_array[:], input_array[:], input_array[:], input_array[:]]
    while True:
        for num in range(5):
            new_input, save_array[num], save_op[num] = run_comp(save_array[num], input_num, perm[num], save_op[num])
            if new_input:
                input_num = new_input
            else:
                break
        if not new_input:
            break
    solutions.append(input_num)
print(max(solutions))
