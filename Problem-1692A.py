n = int(input())
arr = []

for i in range(n):
    n = list(map(int, input().split(" ")))
    arr.append(
        (1 if n[0] < n[1] else 0) + 
        (1 if n[0] < n[2] else 0) +
        (1 if n[0] < n[3] else 0)  
    )

for a in arr:
    print(a)