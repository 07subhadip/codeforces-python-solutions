t = int(input())
arr = []

for i in range(t):
    a, b = map(int, input().split(" "))
    val = float('inf')

    for c in range(a, b+1):
        val = min(val, (c - a) + (b - c))

    arr.append(val)

for a in arr:
    print(a)