num = int(input())
orders = list(input())
count = 0

for i in range(len(orders) - 1):
    if orders[i] == orders[i + 1]:
        count += 1

print(count)