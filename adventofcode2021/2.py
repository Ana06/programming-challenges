directions = {"forward": (1, 0), "down": (0, 1), "up": (0, -1)}
solution = [0, 0]
try:
    while True:
        command, value = input().split()
        value = int(value)
        direction = directions[command]
        solution[0] += direction[0] * value
        solution[1] += direction[1] * value
except EOFError:
    print(solution[0] * solution[1])
