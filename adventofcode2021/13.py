import numpy as np

N = 1500
paper = np.zeros((N, N), dtype=bool)

line = input()
while line:
    dot_y, dot_x = line.split(",")
    paper[int(dot_x), int(dot_y)] = True
    line = input()

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
    print(paper[:x, :y].sum())
    exit()
