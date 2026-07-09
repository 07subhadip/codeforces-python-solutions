import math

t = int(input())
arr = []

for i in range(t):
    n = int(input())
    nums = list(input())

    while len(nums) > 1:
        if nums[0] != nums[-1]:
            nums.pop(0)
            nums.pop(-1)
        else:
            break

    arr.append(len(nums))

        
for a in arr:
    print(a)