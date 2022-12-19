# python 13-2.py input13.txt

import ast
import sys


def parse_packet(line):
    return ast.literal_eval(line[:-1])

def compare(l,r):
    print(l, r)
    if isinstance(l, int) and isinstance(r, int):
        if l == r:
            return 0
        if l < r:
            return 1
        return -1
    
    if isinstance(l, int):
        l = [l]
    if isinstance(r, int):
        r = [r]
    for e1, e2 in zip(l,r):
        if compare(e1, e2):
            return 0
    if len(l) == len(r):
        return 0
    if len(l) < len(r):
        return 1
    return -1


def ordered(left, right):
    compared = 0
    for l, r in zip(left, right):
        compared = compare(l,r)
        if compared:
            break
    if not compared:
        if len(left) < len(right):
            return 1
    return compared

packets =  []
for  line in open(sys.argv[1]):
    if line == "\n":
        continue
    packet = parse_packet(line)
    print(paket)
    index = len(packets)
    for i in range(len(packets)):
        if ordered(packet, packets[i]):
            index = i
            break
    packets = packets[:index] + [packet] + packets[index:]


packet = "[[2]]"
index = len(packets)
for i in range(len(packets)):
    if ordered(packet, packets[i]):
        index = i
        break
packets = packets[:index] + [packet] + packets[index:]


packet = "[[6]]"
index2 = len(packets)
for i in range(len(packets)):
    if ordered(packet, packets[i]):
        index2 = i
        break
print((index+1)*(index2+1))
