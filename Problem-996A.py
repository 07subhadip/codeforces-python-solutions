bill = int(input())
count = 0

while bill != 0:
    if bill >= 100:
        count += bill // 100
        bill = bill % 100
    elif bill >= 20 and bill < 100:
        count += bill // 20
        bill = bill % 20
    elif bill >= 10 and bill < 20:
        count += bill // 10
        bill = bill % 10
    elif bill >= 5 and bill < 10:
        count += bill // 5
        bill = bill % 5
    else:
        count += bill
        bill = 0

print(count)