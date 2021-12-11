import numpy as np
import sys


file_name = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
locations = np.genfromtxt(file_name, delimiter=1, dtype=np.uint8)
shape = locations.shape
flashes = 0


def flash(i, j):
    global flashes
    if i < 0 or i >= shape[0] or j < 0 or j >= shape[1]:
        return
    if locations[i, j] != 0:
        locations[i, j] += 1
    if locations[i, j] > 9:
        locations[i, j] = 0
        flashes += 1
        flash(i - 1, j)
        flash(i + 1, j)
        flash(i, j - 1)
        flash(i, j + 1)
        flash(i - 1, j - 1)
        flash(i - 1, j + 1)
        flash(i + 1, j - 1)
        flash(i + 1, j + 1)


steps = 0
while True:
    steps += 1
    locations += 1
    previous_flashes = flashes
    while np.any(locations > 9):
        for i in range(shape[0]):
            for j in range(shape[1]):
                if locations[i, j] > 9:
                    flash(i, j)
    if flashes - previous_flashes == locations.size:
        print(steps)
        exit()
