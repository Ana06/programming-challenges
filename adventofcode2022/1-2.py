# python 1-2.py input1.txt

import sys

total_calories = 0
elfs = []
for calories in open(sys.argv[1]):
    calories = calories[:-1]  # Remove '\n'
    if calories:
        total_calories += int(calories)
    if not calories:
        elfs.append(total_calories)
        total_calories = 0
elfs.sort(reverse=True)
print(sum(elfs[:3]))
