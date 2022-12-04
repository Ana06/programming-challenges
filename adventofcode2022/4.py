# python 4.py input4.txt

import sys


def contains(range1, range2):
    if range2[0] <= range1[0] and range2[1] >= range1[1]:
        return True
    return False


# "2-4" -> (2,4)
def to_range(s):
    start, end = s.split("-")
    return (int(start), int(end))


overlaps = 0
for line in open(sys.argv[1]):
    elf1, elf2 = [to_range(s) for s in line[:-1].split(",")]
    if contains(elf1, elf2) or contains(elf2, elf1):
        overlaps += 1
print(overlaps)
