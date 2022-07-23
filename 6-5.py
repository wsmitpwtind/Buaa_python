import bisect

dic = input().split(" ")

dic.sort()

sentence = input().split(" ")

for i in sentence:
    a = bisect.bisect(dic, i)
    print(dic[a - 1],end=" ")

