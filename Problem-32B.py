words = input()
nums = []

i = 0
n = len(words)

while i < n:
    if words[i] == "-":
        if words[i + 1] == "-":
            nums.append("2")
            i += 2
        elif words[i + 1] == ".":
            nums.append("1")
            i += 2
    else:
        nums.append("0")
        i += 1

print("".join(nums))