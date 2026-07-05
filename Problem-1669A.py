n = int(input())
arr = []

for i in range(n):
    point = int(input())

    if point >= 1900:
        arr.append(1)
    elif point <= 1899 and point >= 1600:
        arr.append(2)
    elif point <= 1599 and point >= 1400:
        arr.append(3)
    else:
        arr.append(4)

for a in arr:
    print(f"Division {a}")