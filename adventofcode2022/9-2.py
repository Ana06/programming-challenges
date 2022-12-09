# python 9-2.py input9.txt

import sys


def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def update_knot(h, t):
    h1, h2 = h
    t1, t2 = t
    delta1, delta2 = h1 - t1, h2 - t2
    if abs(delta1) > 1 or abs(delta2) > 1:
        t1 += sign(delta1)
        t2 += sign(delta2)
    return (t1, t2)


KNOTS_NUM = 10
D = {"R": (0, 1), "L": (0, -1), "U": (1, 0), "D": (-1, 0)}
knots = [(0, 0) for _ in range(KNOTS_NUM)]
visited = {knots[-1]}
for line in open(sys.argv[1]):
    direction, num = line[:-1].split()
    for _ in range(int(num)):
        d1, d2 = D[direction]
        knots[0] = (knots[0][0] + d1, knots[0][1] + d2)
        for i in range(1, KNOTS_NUM):
            knots[i] = update_knot(knots[i - 1], knots[i])
        visited.add(knots[-1])
print(len(visited))
