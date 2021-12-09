import numpy as np
import sys


file_name = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
locations = np.genfromtxt(file_name, delimiter=1, dtype=np.uint8)
shape = locations.shape
risk_levels = 0

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
            risk_levels += 1 + element

print(risk_levels)
