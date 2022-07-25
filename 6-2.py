list1 = []
list2 = []
stack = []
temp = input()
for i in temp:
    list1.append(i)

temp = input()
for i in temp:
    list2.append(i)

while len(list1) != 0 and len(list2) != 0:
    temp = list1[0]
    list1.pop(0)
    if temp in stack:
        pla = stack.index(temp)
        list1 = list1 + stack[pla:]
        list1.append(temp)
        stack = stack[:pla]
    else:
        stack.append(temp)

    if len(list1) == 0:
        print("Oh, no!")
        for i in list2:
            print(i, end="")
        break

    temp = list2[0]
    list2.pop(0)
    if temp in stack:
        pla = stack.index(temp)
        list2 = list2 + stack[pla:]
        list2.append(temp)
        stack = stack[:pla]
    else:
        stack.append(temp)

    if len(list2) == 0:
        print("Hahaha~")
        for i in list1:
            print(i, end="")
        break

