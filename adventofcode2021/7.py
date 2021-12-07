import sys
import numpy as np


def distance(line, positions):
    return (np.absolute(positions - line)).sum()


file_name = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
positions = np.genfromtxt(file_name, delimiter=",", dtype=np.int32)

cost = int(distance(np.median(positions), positions))
print(cost)
