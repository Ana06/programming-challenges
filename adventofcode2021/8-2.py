# get 0, 6 and 9, all with same number of signals (6)
def get_zero_six_nine(four, one, s1, s2, s3):
    # only 9 has all signals in 4
    if four.difference(s1) == set():
        nine = s1
        unknown = (s2, s3)
    elif four.difference(s2) == set():
        nine = s2
        unknown = (s1, s3)
    elif four.difference(s3) == set():
        nine = s3
        unknown = (s1, s2)

    # 0 has all signals in 1 and 6 not
    if one.difference(unknown[0]) == set():
        zero = unknown[0]
        six = unknown[1]
    else:
        zero = unknown[1]
        six = unknown[0]

    return (zero, six, nine)


# get 2, 3 and five, all with same number of signals (5)
def get_two_three_five(six, s1, s2, s3):
    # all signals of three are in either 2 or 5
    if s1.difference(s2).difference(s3) == set():
        three = s1
        unknown = (s2, s3)
    elif s2.difference(s1).difference(s3) == set():
        three = s2
        unknown = (s1, s3)
    elif s3.difference(s1).difference(s2) == set():
        three = s3
        unknown = (s1, s2)

    # 6 has all signals in 5 but not in 2
    if unknown[0].difference(six) == set():
        five = unknown[0]
        two = unknown[1]
    else:
        five = unknown[1]
        two = unknown[0]

    return (two, three, five)


solution = 0
try:
    while True:
        table = {}
        signals, output = input().split(" | ")
        signals = [frozenset(s) for s in sorted(signals.split(), key=len)]
        one = signals[0]
        seven = signals[1]
        four = signals[2]
        eight = signals[9]

        zero, six, nine = get_zero_six_nine(
            four, one, signals[6], signals[7], signals[8]
        )
        two, three, five = get_two_three_five(six, signals[3], signals[4], signals[5])

        table[zero] = "0"
        table[one] = "1"
        table[two] = "2"
        table[three] = "3"
        table[four] = "4"
        table[five] = "5"
        table[six] = "6"
        table[seven] = "7"
        table[eight] = "8"
        table[nine] = "9"

        output = [frozenset(s) for s in output.split()]
        output_value = ""
        for value in output:
            output_value += table[value]
        solution += int(output_value)

except EOFError:
    print(solution)
