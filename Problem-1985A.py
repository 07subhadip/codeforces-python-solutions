t = int(input())

for i in range(t):
    a, b = list(input().split(" "))

    if a == b:
        print(a, b)
    else:
        c = "".join([a[0], b[1:]])
        d = "".join([b[0], a[1:]])

        print(d, c)