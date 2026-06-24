n = int(input())
count = 0

for i in range(n):
    word = input()

    if word == "Tetrahedron":
        count += 4
    elif word == "Cube":
        count += 6
    elif word == "Octahedron":
        count += 8
    elif word == "Dodecahedron":
        count += 12
    else:
        count += 20

print(count)