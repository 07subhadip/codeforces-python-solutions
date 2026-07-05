n, time = map(int, input().split(" "))
time_have = 240 - time
time_count = 0
count = 0

for i in range(1, n + 1):
    time_count += 5 * i
    if time_count > time_have:
        break

    count += 1

print(count)