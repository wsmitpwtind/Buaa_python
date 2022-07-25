temp = input().split(" ")
k = int(temp[0])
c = int(temp[1])

dp = []

temp = [0]
for i in range(1, 101):
    if i <= c :
        temp.append(1)
    else:
        temp.append(0)
dp.append(temp)

for i in range(1, 100):
    temp = []
    for j in range(0, 101):
        if i + 1 > j:
            temp.append(0)
        elif i + 1 == j:
            temp.append(1)
        else:
            data = 0
            for m in range(j):
                if j - m <= c:
                    data += dp[i - 1][m]
            temp.append(data)
    dp.append(temp)

ans = 0
for i in range(k - 1, 100):
    ans += dp[i][100]

print(ans)
