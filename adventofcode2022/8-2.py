# python 8-2.py input8.txt

import numpy as np
import sys


def seen_trees(trees, tree):
    blocking = trees >= tree
    if blocking.any():
        # argmax -> returns index of first occurrence of maximum
        return np.argmax(blocking) + 1
    else:
        return len(trees)


trees = np.genfromtxt(sys.argv[1], delimiter=1, dtype=np.uint8)
height, width = trees.shape

max_score = 0
for i in range(1, height - 1):
    for j in range(1, width - 1):
        tree = trees[i, j]
        score = (
            seen_trees(trees[i, j + 1 :], tree)
            * seen_trees(np.flip(trees[i, :j]), tree)
            * seen_trees(trees[i + 1 :, j], tree)
            * seen_trees(np.flip(trees[:i, j]), tree)
        )
        max_score = max(max_score, score)
print(max_score)
