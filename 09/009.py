#!/bin/python

with open("input.txt") as f:
    input_array = [int(num) for num in f.read().rstrip().split(',')]

#input_array = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

def run_comp(mem, input_num):
    op = 0
    rel_base = 0
    while op < len(mem):
        if mem[op] == 99:
            print("Halt!")
            break
        opcode = str(mem[op])[-1]
        modes = str(mem[op]).rjust(5, '0')[:3]

        if modes[2] == "2":
            num = mem[op + 1] + rel_base
        elif modes[2] == "1":
            num = op + 1
        elif modes[2] == "0":
            num = mem[op + 1]

        if modes[1] == "2":
            num_2 = mem[op + 2] + rel_base
        elif modes[1] == "1":
            num_2 = op + 2
        elif modes[1] == "0":
            num_2 = mem[op + 2]

        if modes[0] == "2":
            num_3 = mem[op + 3] + rel_base
        elif modes[0] == "0":
            num_3 = mem[op + 3]


        if opcode == "1":
            mem[num_3] = mem[num] + mem[num_2]
        elif opcode == "2":
            mem[num_3] = mem[num] * mem[num_2]
        elif opcode == "3":
            mem[num] = input_num
            op += 2
            continue
        elif opcode == "4":
            print(mem[num])
            op += 2
            continue
        elif opcode == "5":
            if mem[num]:
                op = mem[num_2]
                continue
            else:
                op += 3
                continue
        elif opcode == "6":
            if not mem[num]:
                op = mem[num_2]
                continue
            else:
                op += 3
                continue
        elif opcode == "7":
            if mem[num] < mem[num_2]:
                mem[num_3] = 1
            else:
                mem[num_3] = 0
        elif opcode == "8":
            if mem[num] == mem[num_2]:
                mem[num_3] = 1
            else:
                mem[num_3] = 0
        elif opcode == "9":
            rel_base += mem[num]
            op += 2
            continue
        else:
            print("ERROR")
            print(mem[op])
            exit()
        op += 4
extend = [0] * 999999
input_array.extend(extend)
run_comp(input_array, 1)
run_comp(input_array, 2)
