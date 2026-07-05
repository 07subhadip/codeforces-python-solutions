arr = list(map(int, input().split(" ")))
a_b_c = max(arr)
arr.remove(a_b_c)
# print(arr)

a = a_b_c - arr[0]
b = a_b_c - arr[1]
c = a_b_c - arr[2]

print(a, b, c)