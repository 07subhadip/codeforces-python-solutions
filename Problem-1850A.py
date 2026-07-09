t = int(input())
arr = []

for i in range(t):
    a, b, c = map(int, input().split(" "))

    if a + b >= 10 or a + c >= 10 or b + c >= 10:
        arr.append("YES")
    else:
        arr.append("NO")


for a in arr:
    print(a)