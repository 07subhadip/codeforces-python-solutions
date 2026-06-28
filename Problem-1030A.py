n = int(input())
subs = list(map(int, input().split(" ")))

for sub in subs:
    if sub == 1:
        print("HARD")
        break
else:
    print("EASY")