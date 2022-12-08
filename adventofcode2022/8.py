# python 8.py input8.txt

import numpy as np
import sys

trees = np.genfromtxt(sys.argv[1], delimiter=1, dtype=np.uint8)
height, width = trees.shape

visibles = (height + width) * 2 - 4
for i in range(1, height - 1):
    for j in range(1, width - 1):
        tree = trees[i, j]
        if (
            max(trees[i, :j]) < tree
            or max(trees[i, j + 1 :]) < tree
            or max(trees[:i, j]) < tree
            or max(trees[i + 1 :, j]) < tree
        ):
            visibles += 1
print(visibles)
