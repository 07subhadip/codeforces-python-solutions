n = int(input())
arr = []

for i in range(n):
    word = input()
    arr.append("YES" if word in "codeforces" else "NO")

for a in arr:
    print(a)