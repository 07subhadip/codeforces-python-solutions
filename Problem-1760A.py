t = int(input())
arr = []

for i in range(t):
    a, b, c = map(int, input().split(" "))
    arr.append((a + b + c) - (min(a, b, c) + (max(a, b, c))))

for a in arr:
    print(a)