arr = list(map(int, input().split(" ")))
hashmap = {}
count = 0

for a in arr:
    if a in hashmap:
        count += 1
    else:
        hashmap[a] = 1        

print(count)