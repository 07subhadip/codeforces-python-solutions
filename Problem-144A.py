n = int(input())
nums = list(map(int, input().split(" ")))

low = 0
high = 0
low_so_far = nums[0]
high_so_far = nums[0]

for idx, val in enumerate(nums):
    if val <= low_so_far:
        low_so_far = val
        low = idx

for idx, val in enumerate(nums):
    if val > high_so_far:
        high_so_far = val
        high = idx

# print(low, high)

if low < high:
    print((high + (len(nums) - 1 - low)) - 1)
else:
    print(high + (len(nums) - 1 - low))