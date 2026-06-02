row = 5
matrix = []
m, n = 0, 0

for i in range(row):
    mat = list(map(int, input().split(" ")))
    for j in range(len(mat)):
        if mat[j] == 1:
            m, n = i, j

print(f"{abs(m - 2) + abs(n - 2)}") 