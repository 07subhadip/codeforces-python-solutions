n = int(input())
arr = []

for _ in range(n):
    a, b = list(map(int, input().split(" ")))
    if a % b == 0:
        arr.append(0)
    else:
        arr.append(int(((a // b) + 1) * b) - a)

for a in arr:
    print(a)