import numpy as np

read = []
for j in range(4):
    a = input().split(" ")
    tempList = []
    for i in range(4):
        tempList.append(int(a[i]))
    read.append(tempList)

ma = np.array(read)
print(int(np.linalg.det(ma)))
