echo = []

def generator(x):
    if x == 2:
        for i in range(1, 10):
            echo.append(int(str(i) + str(i)))
    elif x == 3:
        for i in range(1, 10):
            for j in range(0, 10):
                echo.append(int(str(i) + str(j) + str(i)))
    elif x == 4:
        for i in range(1, 10):
            for j in range(0, 10):
                echo.append(int(str(i) + str(j) + str(j) + str(i)))
    elif x == 5:
        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 10):
                    echo.append(int(str(i) + str(j) + str(k) + str(j) + str(i)))
    elif x == 6:
        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 10):
                    echo.append(int(str(i) + str(j) + str(k) + str(k) + str(j) + str(i)))
    elif x == 7:
        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 10):
                    for m in range(0, 10):
                        echo.append(int(str(i) + str(j) + str(k) + str(m) + str(k) + str(j) + str(i)))
    elif x == 8:
        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 10):
                    for m in range(0, 10):
                        echo.append(int(str(i) + str(j) + str(k) + str(m) + str(m) + str(k) + str(j) + str(i)))


n = int(input())
div = []
for i in range(n):
    div.append(int(input()))


for i in range(1, 9):
    generator(i)

zip = True
temp = True
for i in echo:
    temp = True
    for j in div:
        if i % j != 0:
            temp = False
            break
    if temp:
        zip = False
        print(i)

if zip:
    print(None)