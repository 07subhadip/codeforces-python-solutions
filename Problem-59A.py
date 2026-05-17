word = input()

up, low = 0, 0

for ch in word:
    if ch.isupper():
        up += 1
    else:
        low += 1

if up > low:
    print(word.upper())
else:
    print(word.lower())