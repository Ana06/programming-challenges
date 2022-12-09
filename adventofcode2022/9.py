# python 9.py input9.txt

import sys


def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def update_tail(h1, h2, t1, t2):
    delta1, delta2 = h1 - t1, h2 - t2
    if abs(delta1) > 1 or abs(delta2) > 1:
        t1 += sign(delta1)
        t2 += sign(delta2)
    return (t1, t2)


D = {"R": (0, 1), "L": (0, -1), "U": (1, 0), "D": (-1, 0)}
t1 = t2 = h1 = h2 = 0
visited = {(t1, t2)}
for line in open(sys.argv[1]):
    direction, num = line[:-1].split()
    for _ in range(int(num)):
        d1, d2 = D[direction]
        h1 += d1
        h2 += d2
        t1, t2 = update_tail(h1, h2, t1, t2)
        visited.add((t1, t2))
print(len(visited))
