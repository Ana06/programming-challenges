import numpy as np

board = np.zeros((1000, 1000), dtype=np.uint8)
try:
    while True:
        point1, _, point2 = input().split()
        x1, y1 = [int(x) for x in point1.split(",")]
        x2, y2 = [int(x) for x in point2.split(",")]
        points1, points2 = [], []
        while x1 != x2 or y1 != y2:
            board[x1, y1] += 1
            if x1 < x2:
                x1 += 1
            elif x2 < x1:
                x1 -= 1

            if y1 < y2:
                y1 += 1
            elif y2 < y1:
                y1 -= 1

        board[x1, y1] += 1
except EOFError:
    result = (board > 1).sum()
    print(result)
