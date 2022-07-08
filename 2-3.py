from decimal import Decimal

n = int(input())
a = 0
b = 0
c = 0
for i in range(3 * n):
    temp = input().split(" ")
    if len(temp) == 2:
        score = float(temp[0])
        name = temp[1]
        if name == "Chinese":
            a += score
        elif name == "Math":
            b += score
        else:
            c += score

print(Decimal(a / n).quantize(Decimal("0.00")))
print(Decimal(b / n).quantize(Decimal("0.00")))
print(Decimal(c / n).quantize(Decimal("0.00")))
