temp = input().split(" ")
temp = list(set(temp))
temp.sort()
for i in range(len(temp) - 1):
    print(temp[i], end=" ")
print(temp[len(temp) - 1])
