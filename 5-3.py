n = int(input())
listX = []
listY = []
temp = input().split(" ")
for i in range(n):
    listX.append(int(temp[i]))

temp = input().split(" ")
plusAll = 0
for i in range(n):
    listY.append(int(temp[i]))
    plusAll += int(temp[i])

plus = []
minAll = 0
for i in range(n):
    plus.append(plusAll - minAll)
    minAll += int(temp[i])

ans = 0
for i in range(n):
    ans += listX[i] * plus[i]

print(ans)