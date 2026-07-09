n = int(input())
arr = list(map(int, input().split(" ")))
total = 0

if len(arr) <= 1:
    print(0)
else:
    high = max(arr)
    for a in arr:
        total += abs(high - a)

    print(total)