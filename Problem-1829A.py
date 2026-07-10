t = int(input())

for i in range(t):
    s = "codeforces"
    count = 0
    word = input()

    for i in range(10):
        if word[i] != s[i]:
            count += 1

    print(count)
    
