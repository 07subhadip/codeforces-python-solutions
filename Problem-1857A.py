t = int(input())
arr = []


for i in range(t):
    n = int(input())
    nums = list(map(int, input().split(" ")))
    odd = 0
    even = 0
    
    for num in nums:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    arr.append("YES" if odd % 2 == 0 else "NO")

for a in arr:
    print(a)