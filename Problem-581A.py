a, b = map(int, input().split(" "))

rem = (max(a, b) - min(a, b)) // 2

print(f"{min(a, b)} {rem}")