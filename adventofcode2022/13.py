# python 13.py input13.txt

import ast
import sys

f = open(sys.argv[1])

def parse_packet(line):
    return ast.literal_eval(line[:-1])

def compare(l,r):
    global ordered
    if isinstance(l, int) and isinstance(r, int):
        if l == r:
            return False
        if l < r:
            ordered += i
        return True
    
    if isinstance(l, int):
        l = [l]
    if isinstance(r, int):
        r = [r]
    for e1, e2 in zip(l,r):
        if compare(e1, e2):
            return True
    if len(l) == len(r):
        return False
    if len(l) < len(r):
        ordered += i
    return True


line = None
i = 0
ordered = 0
while line != "":
    i += 1
    left = parse_packet(f.readline())
    right = parse_packet(f.readline())
    print(i)
    print(left)
    print(right)
    compared = False
    for l, r in zip(left, right):
        if compare(l,r):
            compared = True
            break
    if not compared:
        if len(left) < len(right):
            ordered += i
    line = f.readline()
print(ordered)
