# python 1.py input1.txt

import sys

total_calories = 0
max_calories = 0
for calories in open(sys.argv[1]):
    calories = calories[:-1]  # Remove '\n'
    if calories:
        total_calories += int(calories)
    if not calories:
        max_calories = max(max_calories, total_calories)
        total_calories = 0
print(max_calories)
