#!/bin/python

from collections import Counter as count

min = 372037
max = 905157

def are_adj(num):
    adj = []
    if num[0] == num[1]:
        adj.append(num[0])
    if num[1] == num[2]:
        adj.append(num[1])
    if num[2] == num[3]:
        adj.append(num[2])
    if num[3] == num[4]:
        adj.append(num[3])
    if num[4] == num[5]:
        adj.append(num[4])
    test = count(adj).values()
    if 1 in test:
        return True
    else:
        return False

def are_small(num):
    if num[0] <= num[1] and num[1] <= num[2] and num[2] <= num[3] and num[3] <= num[4] and num[4] <= num[5]:
        return True

solutions = []
for num in range(min, max + 1):
    num_map = [int(x) for x in str(num)]
    if are_small(num_map) and are_adj(num_map):
            print(num)
            solutions.append(num)

print(len(solutions))
