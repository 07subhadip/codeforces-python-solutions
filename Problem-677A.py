import math

num, h = list(map(int, input().split(" ")))
hts = list(map(int, input().split(" ")))

count = 0

for ht in hts:
    if ht > h:
        count += math.ceil(ht / h)
    else:
        count += 1

print(count)