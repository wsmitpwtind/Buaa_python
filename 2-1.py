temp = input().split(" ")
a1 = int(temp[0])
a2 = int(temp[1])
a3 = int(temp[2])
temp = input().split(" ")
b1 = int(temp[0])
b2 = int(temp[1])
b3 = int(temp[2])
temp = input().split(" ")
c1 = int(temp[0])
c2 = int(temp[1])
c3 = int(temp[2])

print(a1*b2*c3+a2*b3*c1+a3*b1*c2-a3*b2*c1-a2*b1*c3-a1*b3*c2)