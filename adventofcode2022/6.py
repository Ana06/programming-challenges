# python 6.py input6.txt

import sys

datastream = open(sys.argv[1]).read()
for i in range(3, len(datastream)):
    if len(set(datastream[i - 4 : i])) == 4:
        print(i)
        break
