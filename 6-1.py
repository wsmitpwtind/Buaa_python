import math
from decimal import Decimal

n = int(input())

temp = input().split(" ")
x0 = int(temp[0])
y0 = int(temp[1])
dis = []
dis.append([x0, y0])

for i in range(n):
    temp = input().split(" ")
    x = int(temp[0])
    y = int(temp[1])
    tempList = []
    tempList.append(x)
    tempList.append(y)
    dis.append(tempList)


def search(arr, now):
    if len(arr) == n + 1:
        return math.sqrt((dis[now][0] - dis[0][0]) * (dis[now][0] - dis[0][0]) + (dis[now][1] - dis[0][1]) * (
                    dis[now][1] - dis[0][1]))
    tempAns = []
    for i in range(1, n + 1):
        has = False
        for j in range(len(arr)):
            if arr[j] == i:
                has = True
                break
        if not has:
            newArr = arr.copy()
            newArr.append(i)
            theDis = math.sqrt((dis[now][0] - dis[i][0]) * (dis[now][0] - dis[i][0]) + (dis[now][1] - dis[i][1]) * (
                    dis[now][1] - dis[i][1]))
            re = search(newArr, i)
            tempAns.append(re + theDis)
    min = -1
    for i in tempAns:
        if min == -1 or i < min:
            min = i
    if now == 0:
        print(Decimal(min).quantize(Decimal("0.00")))
    return min

ans = []
search([0], 0)
