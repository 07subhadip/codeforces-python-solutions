t = int(input())
arr = []


for i in range(t):
    n = int(input())
    nums = list(map(int, input().split(" ")))
    hashmap = {}
    
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1

    for key, val in hashmap.items():
        if val == 1:
            arr.append(nums.index(int(key)) + 1)


for a in arr:
    print(a)