import numpy as np
from pprint import pprint

N = 1500
paper = np.zeros((N, N), dtype=bool)


def to_char(b):
    if b:
        return "#"
    return " "  # Use space instead of dot as it is easier to read


line = input()
while line:
    dot_y, dot_x = line.split(",")
    paper[int(dot_x), int(dot_y)] = True
    line = input()
try:
    x, y = N, N
    while True:
        text, number = input().split("=")
        number = int(number)
        if text[-1] == "y":  # Fold along y
            x = number
            for i in range(number):
                j = 2 * number - i
                paper[i, :] |= paper[j, :]
        else:  # Fold along x
            y = number
            for i in range(number):
                j = 2 * number - i
                paper[:, i] |= paper[:, j]
except EOFError:
    for line in paper[:x, :y]:
        print("".join(to_char(b) for b in line))
