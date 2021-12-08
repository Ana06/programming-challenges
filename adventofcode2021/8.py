solution = 0
try:
    while True:
        _, output = input().split(" | ")
        values = output.split()
        for value in values:
            if len(value) in (2, 4, 3, 7):
                solution += 1
except EOFError:
    print(solution)
