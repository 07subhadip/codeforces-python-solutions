nums = list(map(int, input()))

count = 0

for num in nums:
    if num == 4 or num == 7:
        count += 1

print("YES" if count == 7 or count == 4 else "NO")