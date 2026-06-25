Limak, Bob = list(map(int, input().split(" ")))

count = 0

while Limak <= Bob:
    count += 1
    Limak = Limak * 3
    Bob = Bob * 2
    

print(count)