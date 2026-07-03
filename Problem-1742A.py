n = int(input())
arr = []

for i in range(n):
    a, b, c = list(map(int, input().split(" ")))

    if a + b == c or a + c == b or b + c == a:
        arr.append("YES") 
    else:
        arr.append("NO")


for a in arr:
    print(a)