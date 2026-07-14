n, k = map(int, input().split())
persons = list(map(int, input().split()))

valids = sum(1 for p in persons if p + k <= 5)

print(valids // 3)