guest = input().upper() 
host = input().upper()
comb = input().upper()

def freq_adder(hashmap, word):
    for w in word:
        if w in hashmap:
            hashmap[w] += 1
        else:
            hashmap[w] = 1
    return hashmap

if len(guest) + len(host) != len(comb):
    print("NO")
else:
    hashmap = {}
    check = {}

    hashmap = freq_adder(hashmap, guest)
    hashmap = freq_adder(hashmap, host)


    check = freq_adder(check, comb)
    

    print("YES" if hashmap == check else "NO")