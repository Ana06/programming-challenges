# python 2-2.py input2.txt

import sys

# Rock (A) defeats Scissors (C)
# Scissors (C) defeats Paper (B)
# Paper (B) defeats Rock (A)
WIN = {"A": "C", "C": "B", "B": "A"}
LOSE = {y: x for x, y in WIN.items()}
SHAPE_POINTS = {"A": 1, "B": 2, "C": 3}

points = 0
for line in open(sys.argv[1]):
    opponent, result = line[:-1].split()
    if result == "Y":  # draw
        points += 3
        points += SHAPE_POINTS[opponent]
    elif result == "Z":  # win
        points += 6
        points += SHAPE_POINTS[LOSE[opponent]]
    else:  # result == "X" # lose
        points += SHAPE_POINTS[WIN[opponent]]
print(points)
