n = int(input())

hashmap = {}

p_i = list(map(int, input().split(" ")))

for i in range(1, n + 1):
    hashmap[p_i[i - 1]] = i

# print(hashmap)

p_i.sort()

# print(p_i)

for a in p_i:
    print(hashmap.get(a), end = " ")