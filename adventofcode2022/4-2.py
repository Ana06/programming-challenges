# python 4-2.py input4.txt

import sys


# "2-4" -> (2,4)
def to_range(s):
    start, end = s.split("-")
    return (int(start), int(end))


overlaps = 0
for line in open(sys.argv[1]):
    elf1, elf2 = [to_range(s) for s in line[:-1].split(",")]
    if min(elf1[1], elf2[1]) >= max(elf1[0], elf2[0]):
        overlaps += 1
print(overlaps)
