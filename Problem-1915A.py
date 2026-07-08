t = int(input())
arr = []

for i in range(t):
    a, b, c = map(int, input().split(" "))

    if a == b:
        arr.append(c)
    elif a == c:
        arr.append(b)
    else:
        arr.append(a)

for a in arr:
    print(a)