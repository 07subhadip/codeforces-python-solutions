num = int(input())
word = input().lower()

hashmap = {}

for ch in word:
    if ch in hashmap:
        hashmap[ch] += 1
    else:
        hashmap[ch] = 1


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for alp in alphabets:
    if alp not in hashmap.keys():
        print("NO")
        break
else:
    print('YES')