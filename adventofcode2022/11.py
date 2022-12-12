# python 11.py input11.txt

import sys
from collections import namedtuple

monkeys = []
Monkey = namedtuple("Monkey", ["i", "items", "operation", "div", "true", "false"])
f = open(sys.argv[1])
while True:
    first_line = f.readline()  # Monkey i
    if not first_line.startswith("Monkey"):
        break
    i = int(first_line[7:-2])
    items = [int(x) for x in f.readline()[18:-1].split(", ")]  # Starting items:
    operation = f.readline()[19:-1]  # Operation: new =
    div = int(f.readline()[21:-1])  # Test: divisible by
    true = int(f.readline()[29:-1])  # Test: divisible by
    false = int(f.readline()[30:-1])  # Test: divisible by
    f.readline()  # Empty line
    monkeys.append(Monkey(i, items, operation, div, true, false))
f.close()

inspected = [0] * len(monkeys)
ROUNDS = 20
for i in range(ROUNDS):
    for monkey in monkeys:
        num_items = len(monkey.items)
        inspected[monkey.i] += num_items
        for _ in range(num_items):
            old = monkey.items.pop()
            new_item = eval(monkey.operation) // 3
            next_monkey = monkey.true if new_item % monkey.div == 0 else monkey.false
            monkeys[next_monkey].items.append(new_item)
    print(f"After round {i+1}")
    for monkey in monkeys:
        print(monkey.items)


inspected = sorted(inspected)
print(inspected[-1] * inspected[-2])
