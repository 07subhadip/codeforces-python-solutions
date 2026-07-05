k, r = map(int, input().split(" "))

count = 1
total = k

while str(total)[-1] != str(r):
    if total % 10 == 0:
        break
    else:
        total += k
        count += 1

print(count)