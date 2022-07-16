dict_b = {
    1: 7,
    2: 9,
    3: 10,
    4: 5,
    5: 8,
    6: 4,
    7: 2,
    8: 1,
    9: 6,
    10: 3,
    11: 7,
    12: 9,
    13: 10,
    14: 5,
    15: 8,
    16: 4,
    17: 2
}
n = int(input())

temp = input().split(" ")
year = int(temp[0])
month = int(temp[1])
day = int(temp[2])

over_18 = 0
incorrect_checksum = 0

for i in range(n):
    temp = input()

    s = 0
    for i in range(17):
        s += int(temp[i]) * dict_b[i + 1]
    s = s % 11
    if temp[17] == 'X':
        s += 10
    else:
        s += int(temp[17])
    if s % 11 != 1:
        incorrect_checksum += 1

    bYear = int(temp[6:10])
    bMouth = int(temp[10:12])
    bDay = int(temp[12:14])
    if bYear < year - 18:
        over_18 += 1
    elif bYear == year - 18:
        if bMouth < month:
            over_18 += 1
        elif bMouth == month:
            if bDay <= day:
                over_18 += 1

print(over_18, end=' ')
print(incorrect_checksum)
