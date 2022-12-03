# python 3.py < input3.txt


def get_priority(item):
    if item >= "a":
        return ord(item) - ord("a") + 1
    return ord(item) - ord("A") + 27


priorities = 0
try:
    while True:
        items = input()
        middle = len(items) // 2
        compartment1, compartment2 = set(items[:middle]), set(items[middle:])
        repeated_item = (compartment1 & compartment2).pop()
        priorities += get_priority(repeated_item)
except EOFError:
    print(priorities)
