# python 3-2.py < input3.txt


def get_priority(item):
    if item >= "a":
        return ord(item) - ord("a") + 1
    return ord(item) - ord("A") + 27


priorities = 0
try:
    while True:
        items1, items2, items3 = set(input()), set(input()), set(input())
        item = (items1 & items2 & items3).pop()
        priorities += get_priority(item)
except EOFError:
    print(priorities)
