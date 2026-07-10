t = int(input())

arr = []
nums = []

for i in range(2000):
    if i % 3 != 0:
        if str(i)[-1] != '3':
            nums.append(i)

for i in range(t):
    n = int(input())
    arr.append(nums[n - 1])

for a in arr:
    print(a)