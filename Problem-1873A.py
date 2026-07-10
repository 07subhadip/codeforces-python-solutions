t = int(input())

for i in range(t):
    words = input()
    mis_placed = 0

    if words[0] != "a": mis_placed += 1
    if words[1] != "b": mis_placed += 1
    if words[2] != "c": mis_placed += 1

    print("YES" if mis_placed <= 2 else "NO")