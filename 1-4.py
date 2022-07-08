from decimal import Decimal

gpas = 0
points = 0
n = int(input())
for i in range(n):
    temp = input().split(" ")
    score = float(temp[0])
    point = float(temp[1])
    if point >= 1:
        if (score >= 60):
            gpas += point * (4 - 3 * (100 - score) ** 2 / 1600)
        else:
            gpas += 0
        points += point
print(Decimal(gpas / points).quantize(Decimal("0.00")))
