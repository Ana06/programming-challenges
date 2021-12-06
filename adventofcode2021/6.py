NUM_DAYS = 256

laterns_list = [int(x) for x in input().split(",")]
laterns = {}
for i in range(9):
    laterns[i] = laterns_list.count(i)

for _ in range(NUM_DAYS):
    new_laterns = laterns[0]
    laterns[0] = laterns[1]
    laterns[1] = laterns[2]
    laterns[2] = laterns[3]
    laterns[3] = laterns[4]
    laterns[4] = laterns[5]
    laterns[5] = laterns[6]
    laterns[6] = laterns[7] + new_laterns
    laterns[7] = laterns[8]
    laterns[8] = new_laterns

print(sum(laterns.values()))
