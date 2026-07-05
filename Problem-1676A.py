n = int(input())

arr = []

for i in range(n):
    nums = list(input())
    left, right = 0, 0

    for a in range(0, 3):
        left += int(nums[a])
        right += int(nums[5 - a])

    arr.append("YES" if left == right else "NO")


for a in arr:
    print(a)