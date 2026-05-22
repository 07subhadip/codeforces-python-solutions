n = int(input())

passenger = 0
max_so_far = 0

for i in range(n):
    down, up = list(map(int, input().split(" ")))
    passenger = (passenger - down) + up
    max_so_far = max(passenger, max_so_far)

print(max_so_far)