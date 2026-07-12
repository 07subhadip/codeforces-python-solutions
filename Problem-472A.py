n = int(input())

def prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

for a in range(2, n):
    b = n - a

    if not prime(a) and not prime(b):
        print(a, b)
        break