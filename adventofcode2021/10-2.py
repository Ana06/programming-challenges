import numpy as np

table = {"(": 1, "[": 2, "{": 3, "<": 4}
pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
scores = []
try:
    while True:
        chars = list(input())
        chunks = []
        incomplete = True
        for char in chars:
            if char in pairs.keys():
                if chunks.pop() != pairs[char]:  # Corrupted!
                    incomplete = False
                    break
            else:
                chunks.append(char)
        if incomplete:
            score = 0
            while chunks:
                score *= 5
                score += table[chunks.pop()]
            scores.append(score)
except EOFError:
    print(int(np.median(scores)))
