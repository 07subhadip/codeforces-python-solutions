n = int(input())
nums = list(map(int, input().split(" ")))

sereja = 0
dima = 0

for i in range(len(nums)):
    m = max(nums[0], nums[-1])
    if i % 2 == 0:
        sereja += m
    else:
        dima += m
        
    nums.remove(m)
    
print(sereja, dima)