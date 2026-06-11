n = int(input())
arr = list(map(int, input().split(" ")))
stack = []
count = 0

for a in arr:
    if a < 0 and not stack:
        count += abs(a)
    elif a < 0 and stack:
        stack[-1] += a
        if stack[-1] == 0:
            stack.pop()
        elif stack[-1] < 0:
            count += abs(stack[-1])
    elif a > 0:
        stack.append(a)

print(count)