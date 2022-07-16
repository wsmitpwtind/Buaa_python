class Country:
    def __init__(self, name):
        self.name = name
        self.medals = [0, 0, 0]
        self.players = []

    def getName(self):
        return self.name

    def addPlayer(self, player):
        self.players.append(player)

    def calMedal(self):
        for player in self.players:
            if player.getMedal() != 0:
                for i in player.getMedal():
                    dis = int(i) - 1
                    self.medals[dis] = self.medals[dis] + 1

        # print(self.medals)

    def getMedals(self):
        return self.medals


class Player:
    def __init__(self, name):
        self.name = name
        self.medals = []

    def addMedal(self, medal):
        self.medals.append(medal)

    def getMedal(self):
        return self.medals

    def getName(self):
        return self.name


n = int(input())
players = {}
countries = {}

for i in range(n):
    temp = input().split(" ")
    country = Country(temp[0])
    countries[temp[0]] = country
    for j in range(1, len(temp)):
        player = Player(temp[j])
        country.addPlayer(player)
        players[temp[j]] = player

m = int(input())
for i in range(m):
    temp = input().split(" ")
    player = players[temp[0]]
    player.addMedal(temp[1])

for i in countries.values():
    i.calMedal()

list1 = sorted(countries.items(), key=lambda item: (-item[1].medals[0], item[0]), reverse=False)

for i in list1:
    print(i[0], end=' ')
    print(i[1].getMedals()[0], end=' ')
    print(i[1].getMedals()[1], end=' ')
    print(i[1].getMedals()[2])

print("-----")

list2 = sorted(countries.items(),
               key=lambda item: (-item[1].medals[0] - item[1].medals[1] - item[1].medals[2], item[0]),
               reverse=False)
for i in list2:
    print(i[0], end=' ')
    print(i[1].getMedals()[0], end=' ')
    print(i[1].getMedals()[1], end=' ')
    print(i[1].getMedals()[2])
