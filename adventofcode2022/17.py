# python 17.py input17.txt

import sys
import numpy as np
import time
N = 2022
# 4 consecutive rocks have total height 4
chamber = np.zeros((N//4*13+13, 9),dtype=int)
chamber[0,:] = 1
chamber[:,0] = 1
chamber[:,8] = 1
height = 0

f = open(sys.argv[1])
pattern = list(f.read()[:-1])
f.close()

ROCKS = ( (np.matrix(([1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]),dtype=int), 1),
          (np.matrix(([0,1,0,0],[1,1,1,0],[0,1,0,0],[0,0,0,0]),dtype=int), 3),
          (np.matrix(([1,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]),dtype=int), 3),
          (np.matrix(([1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]),dtype=int), 4),
          (np.matrix(([1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]),dtype=int), 2))

def intersect(rock, i, j):
    chamber_slice = chamber[i:i+4, j: j+4]
    s_i, s_j = chamber_slice.shape
    rock_slice = rock[0:s_i,0:s_j]
    return (chamber_slice & rock_slice).any()

DIR = { ">": 1, "<": -1}
pattern_i = 0
for rock_i in range(0,N):
    rock, rock_height = ROCKS[rock_i % len(ROCKS)]
    i = height + 4
    j = 3
    while True:
        old_j = j
        j+= DIR[pattern[pattern_i]]
        pattern_i = (pattern_i + 1) % len(pattern)
        if intersect(rock, i, j):
            j = old_j
        if intersect(rock, i-1,j): # Rest
          chamber_slice = chamber[i:i+4, j: j+4]
          s_i, s_j = chamber_slice.shape
          rock_slice = rock[0:s_i,0:s_j]
          chamber[i:i+4,j:j+4] |= rock_slice
          height = max(height, i - 1 + rock_height)
          if height == 3:
              exit()
          break
        i -= 1
print(height)

