import math
from decimal import Decimal


def calc_area(p1, p2, p3):
    a = float(math.sqrt((p2[0] - p3[0]) * (p2[0] - p3[0]) + (p2[1] - p3[1]) * (p2[1] - p3[1])))
    b = float(math.sqrt((p1[0] - p3[0]) * (p1[0] - p3[0]) + (p1[1] - p3[1]) * (p1[1] - p3[1])))
    c = float(math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])))
    return a + b + c


p1 = []
p2 = []
p3 = []
temp = input().split(" ")
for d in temp:
    p1.append(int(d))
temp = input().split(" ")
for d in temp:
    p2.append(int(d))
temp = input().split(" ")
for d in temp:
    p3.append(int(d))
print(Decimal(calc_area(p1, p2, p3)).quantize(Decimal("0.00")))
