#!/bin/python

with open("input.txt") as f:
    lines = [(line2.split(')')[0], line2.split(')')[1]) for line2 in [line.strip() for line in f.readlines()]]
for (tee, ter) in lines:
    if ter == "YOU":
        you_orb = (tee, ter)
    elif ter == "SAN":
        san_orb = (tee, ter)

def bac_orbits(orb):
    orb_list = []
    for (tee, ter) in lines:
        if ter == orb[0]:
            orb_list.append(ter)
            new_start = (tee, ter)
            orb_list.extend(bac_orbits(new_start))
    return(orb_list)

you = bac_orbits(you_orb)
san = bac_orbits(san_orb)
x = -1
for u in you:
    x += 1
    y = -1
    for sa in san:
        y += 1
        if u == sa:
            print(x + y)
            exit()
