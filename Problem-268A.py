n =  int(input())

home = {}
guest = {}
count = 0

for i in range(n):
    h, g = list(map(int, input().split(" ")))
    if h in home:
        home[h] += 1
    else:
        home[h] = 1

    if g in guest:
        guest[g] += 1
    else:
        guest[g] = 1

# print(home, guest) 

for h in home:
    if h in guest:
        count += home[h] * guest[h]


print(count)