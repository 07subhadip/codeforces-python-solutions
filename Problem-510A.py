n, m = list(map(int, input().split(" ")))
right = True

for i in range(n):
    if i % 2 == 0:
        print("#" * m)
    else:
        if right:
            print("." * (m - 1) + "#")
            right = False 
        else:
            print("#" + "." * (m - 1))
            right = True