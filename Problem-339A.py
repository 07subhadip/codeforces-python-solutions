nums = list(map(int, input().split("+")))
nums.sort()

eq = "+".join(list(map(str, nums)))

print(eq)