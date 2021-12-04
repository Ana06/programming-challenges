import sys
import numpy as np


def get_line():
    return [int(x) for x in input().split()]


def has_won(board):
    return np.any(np.all(board == [-1] * 5, axis=0)) or np.any(np.all(board == [-1] * 5, axis=1))


# Solution for both parts 1 and 2, part given as argument
part = int(sys.argv[1]) if len(sys.argv) > 1 else 2
strategy = min if part == 1 else max

numbers = [int(x) for x in input().split(",")]
scores = []
rounds = []
try:
    while True:
        input()  # Read empty line
        board = np.array([get_line(), get_line(), get_line(), get_line(), get_line()], dtype=np.int8)
        for i, number in enumerate(numbers):
            board[board == number] = -1  # Mark drawn number
            if has_won(board):
                board[board == -1] = 0  # Avoid counting marked numbers
                score = board.sum() * number
                scores.append(score)
                rounds.append(i)
                break
except EOFError:
    winning_board = rounds.index(strategy(rounds))
    winning_score = scores[winning_board]
    print(winning_score)
