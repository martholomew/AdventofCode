#!/bin/python

import operator

with open("input.txt") as f:
    image = [int(i) for i in f.read().rstrip()]

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

img_matrices = [[row for row in list(chunks(layer, 25))] for layer in list(chunks(image, 150))]
one_counts = [sum([row.count(0) for row in layer]) for layer in img_matrices]
print(one_counts)
min_index, _ = min(enumerate(one_counts), key=operator.itemgetter(1))
print(img_matrices[min_index])
one = sum([row.count(1) for row in img_matrices[min_index]])
two = sum([row.count(2) for row in img_matrices[min_index]])
print(one * two)
