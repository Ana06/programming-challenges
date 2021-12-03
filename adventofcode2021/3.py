def list_to_int(bitlist):
    result = 0
    for bit in bitlist:
        result = (result << 1) | bit
    return result


bits = list(input())
number_ones = [0] * len(bits)
length = 1
try:
    while True:
        for index, bit in enumerate(bits):
            number_ones[index] += int(bit)
        bits = list(input())
        length += 1
except EOFError:
    gamma = []
    epsilon = []
    for i in number_ones:
        if i > (length / 2):
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
    gama_int = list_to_int(gamma)
    epsilon_int = list_to_int(epsilon)

    print(gama_int * epsilon_int)
