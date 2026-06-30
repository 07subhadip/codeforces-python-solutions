n = int(input())

nums = []

for i in range(n):
    candles = int(input())

    if candles <= 2:
        nums.append(0)
    else:
        nums.append(candles // 2 if candles % 2 == 1 else candles // 2 - 1)

for num in nums:
    print(num)