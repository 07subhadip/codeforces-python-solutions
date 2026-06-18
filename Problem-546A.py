import math
k, n, w = list(map(int, input().split(" ")))
price = 0

for i in range(w):
    price += (i + 1) * k

print((price - n) if price > n else 0)