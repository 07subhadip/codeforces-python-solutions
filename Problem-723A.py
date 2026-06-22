x, y, z = list(map(int, input().split(" ")))

high = max(x, y, z)
low = min(x, y, z)

count = float("inf")

for i in range(low, high + 1):
    dist = abs(x - i) + abs(y - i) + abs(z - i)
    count = min(dist, count)


print(count)