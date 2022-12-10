# python 10.py input10.txt

import sys

CYCLES = (20, 60, 100, 140, 180, 220)
cycle = 0
x = 1
solution = 0

for instruction in open(sys.argv[1]):
    instruction = instruction[:-1]
    if instruction == "noop":
        repeat = 1
        v = 0
    else:
        repeat = 2
        _, v = instruction.split()

    for _ in range(repeat):
        cycle += 1
        if cycle in CYCLES:
            solution += cycle * x

    x += int(v)

print(solution)
