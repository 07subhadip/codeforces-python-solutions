t = int(input())

for i in range(t):
    a, b, c = map(int, input().split(" "))

    if a == b:
        if c % 2 == 0:
            print("Second")
        else:
            print("First")
    elif a > b:
        if a - b > c:
            print("First")
        elif a - b <= c:
            if (a - b) + c % 2 == 0:
                print("Second")
            else:
                print("First")
    else:
        if b - a > c:
            print("Second")
        elif b - a <= c:
            if (b - a) + c % 2 == 0:
                print("First")
            else:
                print("Second")