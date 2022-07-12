def judge(x, y):
    if 0 <= x <= h-1 and 0 <= y <= v-1:
        return 1
    else:
        return 0


def find(x, y):
    if data[x][y] == 1:
        return 1
    d = 1
    tx = x + 1
    ty = y + 0
    if judge(tx, ty) and data[x][y] > data[tx][ty]:
        d = max(d, find(tx, ty) + 1)

    tx = x + 0
    ty = y + 1
    if judge(tx, ty) and data[x][y] > data[tx][ty]:
        d = max(d, find(tx, ty) + 1)

    tx = x - 1
    ty = y + 0
    if judge(tx, ty) and data[x][y] > data[tx][ty]:
        d = max(d, find(tx, ty) + 1)

    tx = x + 0
    ty = y - 1
    if judge(tx, ty) and data[x][y] > data[tx][ty]:
        d = max(d, find(tx, ty) + 1)

    data[x][y] = d
    return data[x][y]


temp = input().split(" ")
h = int(temp[0])
v = int(temp[1])
data = []

for i in range(h):
    temp = input().split(" ")
    height = []
    for j in range(v):
        height.append(int(temp[j]))
    data.append(height)

ans = 0

for i in range(h):
    for j in range(v):
        ans = max(ans, find(i, j))

print(ans)
