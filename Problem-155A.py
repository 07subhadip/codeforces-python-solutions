n = int(input())
nums = list(map(int, input().split(" ")))

max_so_far = nums[0]
min_so_far = nums[0]
count = 0

for num in nums:
    if num > max_so_far:
        max_so_far = num
        count += 1
    
    if num < min_so_far:
        min_so_far = num
        count += 1

print(count)