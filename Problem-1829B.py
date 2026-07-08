t = int(input())
arr = []

for i in range(t):
    n = int(input())
    nums = list(map(int, input().split(" ")))

    max_so_far = 0
    curr = 0

    for num in nums:
        if num == 0:
            curr += 1
            max_so_far = max(curr, max_so_far)
        else:
            curr = 0

    arr.append(max_so_far)

for a in arr:
    print(a)