n = int(input())

hate = "I hate"
love = "I love"

sentence = []

if n == 1:
    print(hate + " it", end = "")
else:
    for i in range(n):
        if i % 2 == 0:
            sentence.append(hate)
        else:
            sentence.append(love)

    print(" that ".join(sentence) + " it", end = "")