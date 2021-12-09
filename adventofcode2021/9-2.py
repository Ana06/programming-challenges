import numpy as np
import sys


file_name = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
locations = np.genfromtxt(file_name, delimiter=1, dtype=np.uint8)
shape = locations.shape


def get_basin(point):
    previous_points = set()
    new_points = {point}

    basin = 0
    while new_points:
        point = new_points.pop()
        previous_points.add(point)
        if (
            point[0] >= 0
            and point[0] < shape[0]
            and point[1] >= 0
            and point[1] < shape[1]
            and locations[point] != 9
        ):
            basin += 1
            neighbor_points = {
                (point[0] - 1, point[1]),
                (point[0] + 1, point[1]),
                (point[0], point[1] - 1),
                (point[0], point[1] + 1),
            }
            new_points.update(neighbor_points - previous_points)
    return basin


low_points = []

for i in range(shape[0]):
    for j in range(shape[1]):
        smallest = True
        element = locations[i, j]
        if i - 1 >= 0:
            if element >= locations[i - 1, j]:
                smallest = False
        if i + 1 < shape[0]:
            if element >= locations[i + 1, j]:
                smallest = False
        if j - 1 >= 0:
            if element >= locations[i, j - 1]:
                smallest = False
        if j + 1 < shape[1]:
            if element >= locations[i, j + 1]:
                smallest = False
        if smallest:
            low_points.append((i, j))

basins = sorted([get_basin(low_point) for low_point in low_points])
print(basins[-1] * basins[-2] * basins[-3])
