import numpy as np

board = np.zeros((1000, 1000), dtype=np.uint8)
try:
    while True:
        point1, _, point2 = input().split()
        x1, y1 = [int(x) for x in point1.split(",")]
        x2, y2 = [int(x) for x in point2.split(",")]
        if y1 == y2 or x1 == x2:
            if y2 < y1:
                y1, y2 = y2, y1
            if x2 < x1:
                x1, x2 = x2, x1
            board[range(x1, x2 + 1), range(y1, y2 + 1)] += 1
except EOFError:
    result = (board > 1).sum()
    print(result)
