from decimal import Decimal

temp = input().split(" ")
n = int(temp[0])
k = int(temp[1])
list1 = []
list2 = []

for i in range(1, n + 1):
    if i % k == 0:
        list1.append(i)
    else:
        list2.append(i)

t = 0.0
for i in range(len(list1)):
    t += list1[i]
print(Decimal(t / len(list1)).quantize(Decimal("0.0")), end=" ")
t = 0.0
for i in range(len(list2)):
    t += list2[i]
print(Decimal(t / len(list2)).quantize(Decimal("0.0")))
