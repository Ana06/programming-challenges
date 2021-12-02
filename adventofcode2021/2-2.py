horizontal = 0
depth = 0
aim = 0
try:
    while True:
        command, value = input().split()
        value = int(value)
        if command == "down":
            aim += value
        elif command == "up":
            aim -= value
        elif command == "forward":
            horizontal += value
            depth += aim * value
except EOFError:
    print(horizontal * depth)
