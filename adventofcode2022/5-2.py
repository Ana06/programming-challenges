# python 5-2.py input5.txt

import sys
import re

file = open(sys.argv[1])
num_stacks = len(file.readline()) // 4
stacks = [[] for _ in range(num_stacks)]
file.seek(0)

for line in file:
    if not "[" in line:
        file.readline()
        break
    for i in range(num_stacks):
        crate = line[i * 4 + 1]
        if crate != " ":
            stacks[i].append(line[i * 4 + 1])

for stack in stacks:
    stack.reverse()


for line in file:
    m = re.match("move (?P<num>\d+) from (?P<origin>\d+) to (?P<dest>\d+)", line)
    num = int(m.group("num"))
    origin = int(m.group("origin")) - 1
    dest = int(m.group("dest")) - 1
    stacks[dest] += stacks[origin][-num:]
    stacks[origin] = stacks[origin][:-num]
file.close()

solution = ("").join(stack[-1] for stack in stacks)
print(solution)
