from os import truncate
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

hashmap = {}

for i in range(1, d + 1):
    hashmap[i] = False

for i in range(1, d + 1):
    if i % k == 0:
        hashmap[i] = True
    if i % l == 0:
        hashmap[i] = True
    if i % m == 0:
        hashmap[i] = True
    if i % n == 0:
        hashmap[i] = True

count = 0

for val in hashmap.values():
    if val == True:
        count += 1

print(count) 