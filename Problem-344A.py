n = int(input())
groups = 1
prev = int(input())

for i in range(1, n):
    now = int(input())
    if now != prev:
        groups += 1
    prev = now

print(groups)