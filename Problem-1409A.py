t = int(input())
arr = []

for i in range(t):
    a, b = map(int, input().split(" "))

    if a == b:
        arr.append(0)
    else:
        gap = abs(b - a)
        count = 0

        while gap > 0:
            if gap >= 10:
                count += gap // 10
                gap %= 10
            else:
                gap = 0
                count += 1
        arr.append(count)

for a in arr:
    print(a)