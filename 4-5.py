global queen
global number
queen = []
for i in range(8):
    queen.append([])
number = 0

temp = input().split(" ")
x = int(temp[0])
y = int(temp[1])


def addOne():
    global number
    number += 1


def check(row, col):
    global queen
    i = 0
    atk = False
    while not atk and i < col:
        offset_col = abs(i - col)
        offset_row = abs(int(queen[i]) - row)
        if queen[i] == row or offset_row == offset_col:
            atk = 1
        i = i + 1
    return atk


def decide_position(value):
    global queen
    i = 0
    while i < 8:
        if not check(i, value):
            queen[value] = i
            if value == 7 and queen[x - 1] == y - 1:
                addOne()
            else:
                decide_position(value + 1)
        i = i + 1


decide_position(0)
print(number)
