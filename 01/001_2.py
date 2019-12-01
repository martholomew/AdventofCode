#!/bin/python

with open("input.txt", "r") as f:
    fuel = 0
    for line in f:
        add_fuel = int(line) // 3 - 2
        fuel += add_fuel
        while add_fuel > 0:
            add_fuel = add_fuel // 3 - 2
            if add_fuel > 0:
                fuel += add_fuel
print(fuel)
