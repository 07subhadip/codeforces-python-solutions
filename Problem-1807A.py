n = int(input())
arr = []

for i in range(n):
    nums = list(map(int, input().split(" ")))
    if nums[0] + nums[1] == nums[2]:
        arr.append("+")
    else:
        arr.append("-")

for a in arr:
    print(a)