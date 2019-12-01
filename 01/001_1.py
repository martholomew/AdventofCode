#!/bin/python

with open("input.txt", "r") as f:
    fuel = 0
    for line in f:
        fuel += int(line) // 3 - 2
print(fuel)
