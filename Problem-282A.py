num = int(input())
x = 0

for i in range(num):
    ops = input()
    if ops == "X++" or ops == "++X":
        x += 1
    elif ops == "X--" or ops == "--X":
        x -= 1


print(x)