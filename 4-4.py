x = int(input())
m = input()
n = input()
a = []
b = []
l1 = []

for i in m:
    a.append(int(i))

for j in n:
    b.append(int(j))

a.reverse()
b.reverse()

if len(b) > len(a):
    for i in range(len(b) - len(a)):
        a.append(0)
elif len(a) > len(b):
    for i in range(len(a) - len(b)):
        b.append(0)

temp = 0
for j in range(len(a)):
    c = a[j] + b[j] + temp
    if c >= x:
        l1.append(c % x)
        temp = 1
    else:
        l1.append(c)
        temp = 0
if temp == 1:
    print("1", end='')
l2 = l1[::-1]
for k in range(len(l2)):
    print(l2[k], end='')
