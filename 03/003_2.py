#!/bin/python

from pprint import pprint
import json
import csv

with open("data_1.tsv") as f:
    wire_one_coords = csv.reader(f, delimiter=',')
    wire_one_coords = [this for this in wire_one_coords]
with open("data_2.tsv") as f:
    wire_two_coords = csv.reader(f, delimiter=',')
    wire_two_coords = [this for this in wire_two_coords]

def find_coords(wire_coords):
    coords = {(0,0)}
    for coord in wire_coords[0]:
        x = 0
        y = 0
        step = 0
        direc = coord[:1]
        dist = int(coord[1:])
        if direc == "U":
            y = dist
        elif direc == "D":
            y = -dist
        elif direc == "R":
            x = dist
        elif direc == "L":
            x = -dist
        if x:
            orig = coords[-1][0]
            if x > 0:
                for num in range(x + 1):
                    newcoord = (orig + num, coords[-1][1])
                    step += 1
                    coords[step] = newcoord
            elif x < 0:
                for num in reversed(range(x, 0)):
                    newcoord = (orig + num, coords[-1][1])
                    step += 1
                    coords[step] = newcoord
        elif y:
            orig = coords[-1][1]
            if y > 0:
                for num in range(y + 1):
                    newcoord = (coords[-1][0], orig + num)
                    step += 1
                    coords[step] = newcoord
            elif y < 0:
                for num in reversed(range(y, 0)):
                    newcoord = (coords[-1][0], orig + num)
                    step += 1
                    coords[step] = newcoord

    return(coords)

wire_one = find_coords(wire_one_coords)
wire_two = find_coords(wire_two_coords)
print("done")
results = set(wire_one) & set(wire_two)
print(results)
result = [abs(coords[0]) + abs(coords[1]) for coords in results if coords != (0, 0)]
print(min(result))
#pprint(sorted(steps)[::-1])
