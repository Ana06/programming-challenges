solution = 0
try:
    first = int(input())
    while True:
        second = int(input())
        if second > first:
            solution += 1
        first = second
except EOFError:
    print(solution)
