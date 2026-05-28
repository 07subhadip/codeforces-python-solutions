n, k = list(map(int, input().split(" ")))
scores = list(map(int, input().split(" ")))
count = 0
val = scores[k-1]

for score in scores:
    if score >= val and score > 0:
        count += 1

print(count)
