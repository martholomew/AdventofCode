#!/bin/python

with open("input.txt") as f:
    lines = [(line2.split(')')[0], line2.split(')')[1]) for line2 in [line.strip() for line in f.readlines()]]
for (tee, ter) in lines:
    for (tee_comp, ter_comp) in lines:
        if tee == ter_comp:
            break
        if tee_comp == lines[-1][0]:
            start = (tee, ter)

def find_orbits(start, stupid):
    orbit = 0
    stupid += 1
    for (tee, ter) in lines:
        if tee == start[1]:
            orbit += 1 + stupid
            new_start = (tee, ter)
            orbit += find_orbits(new_start, stupid)
    return(orbit)

orbits = 1
stupid = 0
orbits += find_orbits(start, stupid)
print(orbits)
