word = input()
if word == "{}":
    print(0)
else:
    alpha = set(word[1:-1].split(", "))
    print(len(alpha) if alpha else 0)