n = int(input())
student = {
    1: 0,
    2: 0,
    3: 0,
    10: [],
    20: [],
    30: [],
}

nums = list(map(int, input().split(" ")))

for idx, num in enumerate(nums):
    student[num] += 1
    student[num * 10].append(idx + 1)

t = min(student[1], student[2], student[3])
print(t)

for i in range(t):
    print(student[10][i], student[20][i], student[30][i])