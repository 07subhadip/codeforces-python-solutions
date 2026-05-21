str1 = input().lower()
str2 = input().lower()

for i in range(len(str1)):
    if ord(str1[i]) > ord(str2[i]):
        print(1)
        break
    elif ord(str1[i]) < ord(str2[i]):
        print(-1)
        break
else:
    print(0)