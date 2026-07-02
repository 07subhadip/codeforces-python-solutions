n = int(input())
arr = []

for i in range(n):
    word = input().lower()
    arr.append("YES" if word == "yes" else "NO")

for a in arr:
    print(a)