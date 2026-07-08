t = int(input())
ans = []

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()

    for j in range(n-1):
        if abs(arr[j] - arr[j + 1]) > 1:
            ans.append("NO")
            break
    else:
        ans.append("YES")

for a in ans:
    print(a)