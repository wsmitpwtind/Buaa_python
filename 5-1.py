import re

word = input()

line = input()

it = re.finditer(r'' + word, line, re.I)
temp = re.split(r'' + word, line, 0, re.I)

i = 0
for match in it:
    if temp[i] != '':
        print(temp[i], end=" ")
    else:
        print(temp[i], end="")
    print(match.group(), end=" ")
    i += 1
print(temp[i])