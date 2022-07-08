time = []
temp = input().split(" ")
for num in temp:
    time.append(int(num))

study = int(input())
time[1] += study
while time[1] >= 60:
    time[0] += 1
    time[1] -= 60

if time[0] > 23:
    print("23:30")
elif time[0] == 23 and time[1] > 30:
    print("23:30")
else:
    if time[0] < 10:
        print("0", end="")
    print(time[0], end=":")
    if time[1] < 10:
        print("0", end="")
    print(time[1])
