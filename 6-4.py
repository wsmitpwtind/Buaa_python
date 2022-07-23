temp = input().split(" ")
n = int(temp[0])
m = int(temp[1])

dic = {"grape": 1, "cherry": 2, "orange": 3, "lemon": 4,
       "kiwifruit": 5, "tomato": 6, "peach": 7, "pineapple": 8, "coconut": 9, "watermelon": 10, "WATERMELON": 11}

dic2 = {1: "grape", 2: "cherry", 3: "orange", 4: "lemon",
        5: "kiwifruit", 6: "tomato", 7: "peach", 8: "pineapple", 9: "coconut", 10: "watermelon", 11: "WATERMELON"}
container = []


def gen():
    if len(container) >= 2:
        if container[-1] == container[-2] and container[-1] != 11:
            n = container[-1]
            del container[-1]
            del container[-1]
            container.append(n + 1)
            gen()


ans = False
for i in range(m):
    temp = input()
    code = dic[temp]
    container.append(code)
    gen()
    if len(container) > n:
        ans = False
        break
    elif container.count(11) > 0:
        ans = True
        break
if ans:
    print("You win!")
else:
    print("You lose!")
for i in range(min(n, len(container))):
    print(dic2[container[i]], end=' ')
