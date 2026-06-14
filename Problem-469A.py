n = int(input())
X = list(map(int, input().split(" ")))
Y = list(map(int, input().split(" ")))

X_Y = set(X[1:] + Y[1:])
# print(X_Y)

for i in range(1, n + 1):
    if i not in X_Y:
        print("Oh, my keyboard!")
        break
else:
    print("I become the guy.")