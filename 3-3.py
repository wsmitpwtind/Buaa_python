import re

string = input()
string = string.replace("english", "English")
string = string.replace("...", "wsmitpwtind")
string = string.replace(" u ", " you ")
string = string.replace(" u", " you")
string = string.replace(" u!", " you!")
string = string.replace(" u?", " you?")
string = string.replace(" u.", " you.")
string = re.sub('^u', 'You', string)
string = re.sub('\?u', '?You', string)
string = re.sub('!u', '!You', string)
string = re.sub('\.u', '.You', string)
string = string.replace("..", ".")
string = string.replace("wsmitpwtind", "...")

w = True
for i in string:
    if w and i != ' ':
        w = False
        print(i.upper(), end="")
    elif i == "." or i == "!" or i == "?":
        w = True
        print(i, end="")
    else:
        print(i, end="")
