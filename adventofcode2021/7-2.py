import sys
import numpy as np
import math


def triangular_number(n):
    return n * (n + 1) // 2


def distance(line, positions):
    return sum(triangular_number(abs(pos - line)) for pos in positions)


file_name = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
positions = np.genfromtxt(file_name, delimiter=",", dtype=np.int32)

# solutions of [min_x sum_i triangular_number(|x_i - x|)] is +- 1/2 from mean
mean = np.mean(positions)
candidates = range(math.floor(mean - 1 / 2), math.ceil(mean + 1 / 2) + 1)
cost = min(distance(i, positions) for i in candidates)
print(cost)
