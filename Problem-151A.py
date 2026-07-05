n, k, l, c, d, p, nl, np = map(int, input().split(" "))

drink = (l * k) // nl
lime = (c * d) / 1
salt = p // np

print(int(min(drink, lime, salt) // n))