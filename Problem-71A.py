num = int(input())
words = []

for i in range(num):
    words.append(input())


for word in words:
    if len(word) <= 10:
        print(word)
    else:
        print(f"{word[0]}{len(word) - 2}{word[-1]}")