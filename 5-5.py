cost = []
n = int(input())
buy = []
sell = []
pre = []
temp = input().split(" ")
for i in range(n):
    buy.append(int(temp[i]))
temp = input().split(" ")
for i in range(n):
    sell.append(int(temp[i]))
temp = input().split(" ")
for i in range(n):
    pre.append(int(temp[i]))

cost.append([buy[0] + pre[0]])
for i in range(1, n):
    temp = []
    min = -1
    for j in range(i):
        if min == -1 or cost[i - 1][j] - sell[j] + buy[i] < min:
            min = cost[i - 1][j] - sell[j] + buy[i]
    temp.append(min + pre[0])

    for j in range(1, i + 1):
        temp.append(cost[i-1][j-1] + pre[j])
    cost.append(temp)

min = -1
for i in range(n):
    if min == -1 or cost[n-1][i] - sell[i] < min:
        min = cost[n-1][i] - sell[i]

print(min)


