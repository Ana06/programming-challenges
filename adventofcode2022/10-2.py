# python 10-2.py input10.txt

import sys

HEIGHT, WIDTH = 6, 40
cycle = 0
x = 1
pixels = ""

for instruction in open(sys.argv[1]):
    instruction = instruction[:-1]
    if instruction == "noop":
        repeat = 1
        v = 0
    else:
        repeat = 2
        _, v = instruction.split()

    for _ in range(repeat):
        if (cycle % WIDTH) in range(x - 1, x + 2):
            pixels += "#"
        else:
            pixels += "."
        cycle += 1

    x += int(v)

for i in range(HEIGHT):
    print(pixels[i * WIDTH : (i + 1) * WIDTH])
