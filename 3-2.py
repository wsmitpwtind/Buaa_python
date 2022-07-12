temp = input()
for i in temp:
    if ord(i) < 100 :
        print("0", end="")
    print(ord(i),end="")