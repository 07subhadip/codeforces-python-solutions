n = int(input())
arr = []

for i in range(n):
    n, k = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))
    arr.append("YES" if k in nums else "NO")

for a in arr:
    print(a)