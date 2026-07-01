n = int(input())

for i in range(n):
    num = int(input())
    size = len(str(num))
    div = 0
    count = 0

    arr = []

    if size > 1:
        div = 10 ** (size - 1)
    else:
        count = 1
        if num > 0:
            arr.append(num)

    while num >= 10:
        count += 1
        arr.append((num // div) * div)
        num = num % div

        if len(str(num)) > 1:
            div = 10 ** (len(str(num)) - 1) 
        else:
            if num > 0:
                count += 1
                arr.append(num)

    print(count)
    for a in arr:
        print(a, end = " ")

    print()