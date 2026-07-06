n = int(input())
arr = []

for i in range(n):
    n, k = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))

    if nums == sorted(nums):
        arr.append("YES")
    elif k < 2:
        arr.append("NO")
    else:
        arr.append("YES")

for a in arr:
    print(a)