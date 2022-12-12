# python 12.py input12.txt

import sys


def possible(x1, y1, x2, y2, depth):
    if x2 < 0 or x2 >= X or y2 < 0 or y2 >= Y:
        return False
    if (x2, y2) in explored:
        return False
    if ord(heightmap[x1][y1]) + 1 >= ord(heightmap[x2][y2]):
        return True
    return False


heightmap = []
for line in open(sys.argv[1]):
    heightmap.append(list(line[:-1]))
X, Y = len(heightmap), len(heightmap[0])

for x in range(X):
    for y in range(Y):
        if heightmap[x][y] == "S":
            start = (x, y)
            heightmap[x][y] = "a"
        if heightmap[x][y] == "E":
            goal = (x, y)
            heightmap[x][y] = "z"

explored = {start}
to_explore = [(start[0], start[1], 0)]  # x,y, depth
D = ((0, 1), (0, -1), (1, 0), (-1, 0))
while to_explore:
    x, y, depth = to_explore.pop(0)  # BFS
    for dx, dy in D:
        x2, y2 = x + dx, y + dy
        if possible(x, y, x2, y2, depth):
            if (x, y) == goal:
                print(depth + 1)
                exit()
            to_explore.append((x2, y2, depth + 1))
            explored.add((x2, y2))
