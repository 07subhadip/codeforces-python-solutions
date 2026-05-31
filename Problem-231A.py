n = int(input())
total = 0

for i in range(n):
    nums = list(map(int, input().split(" ")))
    total += 1 if sum(nums) >= 2 else 0

print(total)