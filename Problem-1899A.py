n = int(input())
arr = []

for i in range(n):
    num = int(input())

    if num % 3 == 0:
        arr.append("Second")
    else:
        arr.append("First")

for a in arr:
    print(a)