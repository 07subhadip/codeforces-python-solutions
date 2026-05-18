n = input()
m = input()

ans = ""

for a, b in zip(n, m):
    if a == b:
        ans += "0"
    else:
        ans += "1"

print(ans)