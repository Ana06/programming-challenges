import numpy as np
import sys


def list_to_int(bitlist):
    result = 0
    for bit in bitlist:
        result = (result << 1) | bit
    return result


file_name = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
matrix = np.genfromtxt(file_name, delimiter=1, dtype=np.uint8)

oxygen = matrix
index = 0
while len(oxygen) > 1:
    most_common = 1 if sum(oxygen[:, index]) >= len(oxygen) / 2 else 0
    oxygen = oxygen[oxygen[:, index] == most_common]
    index += 1

scrubber = matrix
index = 0
while len(scrubber) > 1:
    most_common = 1 if sum(scrubber[:, index]) < len(scrubber) / 2 else 0
    scrubber = scrubber[scrubber[:, index] == most_common]
    index += 1

oxygen_int = list_to_int(oxygen[0])
scrubber_int = list_to_int(scrubber[0])
print(oxygen_int * scrubber_int)
