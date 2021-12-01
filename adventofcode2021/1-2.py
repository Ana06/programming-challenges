solution = 0
try:
    first = int(input())
    second = int(input())
    third = int(input())
    measurements = [first + second + third, second + third, third, 0]
    while True:
        current = int(input())
        for i in range(1, 4):
            measurements[i] += current
        if measurements.pop(0) < measurements[0]:
            solution += 1
        measurements.append(0)
except EOFError:
    print(solution)
