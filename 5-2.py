temp = input().split(" ")
m = int(temp[0])
n = int(temp[1])
t = int(temp[2])
people = []
for i in range(m):
    people.append(True)
for i in range(1, m * t + 1):
    if i % n == 0:
        people[i % m - 1] = False
    if i % 10 == n:
        people[i % m - 1] = False
    if (i % 100) // 10 == n:
        people[i % m - 1] = False
    if (i % 1000) // 100 == n:
        people[i % m - 1] = False
    if (i % 10000) // 1000 == n:
        people[i % m - 1] = False
    if (i % 100000) // 10000 == n:
        people[i % m - 1] = False
    if (i % 1000000) // 100000 == n:
        people[i % m - 1] = False


allFalse = True
for i in range(len(people)):
    if people[i]:
        allFalse = False
        print(i + 1, end=" ")

if allFalse:
    print('NO')