n = int(input())
if n % 2 == 0:
    for i in range(n) :
        for j in range(n) :
            if j+i < n - 1:
                print(" ", end='')
            else:
                print("\"", end='')
        print('')
else:
    for i in range(n) :
        for j in range(n) :
            if j+i < n - 1:
                print(" ", end='')
            else:
                print("\\", end='')
        print('')