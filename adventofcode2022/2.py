# python 2.py input2.txt

import sys

# Rock (X) defeats Scissors (C)
# Scissors (Z) defeats Paper (B)
# Paper (Y) defeats Rock (A)
WIN = (["C", "X"], ["B", "Z"], ["A", "Y"])
DIF_X_A = ord("X") - ord("A")
SHAPE_POINTS = {"X": 1, "Y": 2, "Z": 3}

points = 0
for line in open(sys.argv[1]):
    game = line[:-1].split()  # game = [opponent, me]
    points += SHAPE_POINTS[game[1]]
    if ord(game[0]) + DIF_X_A == ord(game[1]):  # draw
        points += 3
    if game in WIN:  # win
        points += 6
print(points)
