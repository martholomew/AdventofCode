#!/bin/python

import operator
from pprint import pprint

with open("input.txt") as f:
    image = [int(i) for i in f.read().rstrip()]

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

img_matrices = [[row for row in list(chunks(layer, 25))] for layer in list(chunks(image, 150))]
img = [[None for y in range(25)]for x in range(6)]
for layer in img_matrices:
    for row in range(len(layer)):
        for num in range(len(layer[row])):
            if layer[row][num] == 2:
                new_num = None
            else:
                new_num = layer[row][num]
            if img[row][num] == None:
                img[row][num] = new_num
pprint(img)
