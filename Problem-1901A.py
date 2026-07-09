t = int(input())
arr = []

for i in range(t):
    n, x = map(int, input().split(" "))
    gas = list(map(int, input().split(" ")))
    gas.append(x)
    gas.insert(0, 0)
    # print(gas)

    max_so_far = 0

    for idx, val in enumerate(gas):
        if idx == 0:
            continue
        else:
            dist = val - gas[idx - 1]
            # print(dist)

            if idx == len(gas) - 1:
                max_so_far = max(max_so_far, dist * 2) 
            else:
                max_so_far = max(max_so_far, dist)

    arr.append(max_so_far)

for a in arr:
    print(a)