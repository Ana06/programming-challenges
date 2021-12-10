table = {")": 3, "]": 57, "}": 1197, ">": 25137}
pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
result = 0
try:
    while True:
        chars = list(input())
        chunks = []
        for char in chars:
            if char in pairs.keys():
                if chunks.pop() != pairs[char]:  # Corrupted!
                    result += table[char]
                    break
            else:
                chunks.append(char)
except EOFError:
    print(result)
