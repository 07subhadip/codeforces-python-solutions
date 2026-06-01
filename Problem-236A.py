name = input().lower()

if len(set(name)) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")