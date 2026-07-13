from fractions import Fraction


a, b = map(int, input().split(" "))

rem = 7 - max(a, b)

fraq = Fraction(numerator = rem, denominator = 6)

if rem / 6 == 0:
    print(f"0/1")
elif rem / 6 == 1:
    print(f"1/1")
else:
    print(f"{fraq.numerator}/{fraq.denominator}")