# python 6-2.py input6.txt

import sys

CHARS = 14
datastream = open(sys.argv[1]).read()
for i in range(CHARS - 1, len(datastream)):
    if len(set(datastream[i - CHARS : i])) == CHARS:
        print(i)
        break
