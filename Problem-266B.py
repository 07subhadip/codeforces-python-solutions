students, t = list(map(int, input().split(" ")))
order = list(input())

left, right = 0, 1

for i in range(t):
    j = 0
    while j < len(order) - 1:
        if order[j] == "B" and order[j + 1] == "G":
            order[j] = "G"
            order[j + 1] = "B"
            j += 2
        else:
            j += 1

print("".join(order))



