year = int(input())

def check_year(saal: int) -> bool:
    year = list(str(saal))
    freq = {}

    for y in year:
        if y in freq:
            freq[y] += 1
        else:
            freq[y] = 1

    for key in freq.keys():
        if freq[key] > 1:
            return False
    else:
        return True

while True:
    year += 1
    if check_year(year):
        break

print(year)
