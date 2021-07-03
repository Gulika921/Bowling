import random


class Player:

    def __init__(self, name):
        self.name = name
        self.list_of_frame = []

    @property
    def score(self):
        if self.list_of_frame[-1][-1] == "X":
            return "X"
        elif self.list_of_frame[-1][-1] == "/":
            return "/"
        list_of_values = []
        for i in self.list_of_frame:
            list_of_values += i
        if sum(list_of_values) < 300:
            return sum(list_of_values)
        else:
            raise SystemExit("Maximum points are 300")  # or print("Maximum points are 300")

    def first_pre_check(self, throw):
        if len(self.list_of_frame) > 1:
            if self.list_of_frame[-2][-1] == "X":
                self.list_of_frame[-2][-1] = 20+throw
        if self.list_of_frame[-1][-1] == "/":
            self.list_of_frame[-1][-1] = 10+throw

    def second_pre_check(self, throw1, throw2):
        if self.list_of_frame[-1][-1] == "X":
            self.list_of_frame[-1][-1] = 10 + throw1 + throw2

    def check_first_throw(self, throw: int):
        """Return int type or string type"""
        if throw >= 10:
            if self.list_of_frame:
                self.first_pre_check(throw)
            self.list_of_frame += [["X"]]
            return "X"
        if self.list_of_frame:
            self.first_pre_check(throw)
        return throw

    def check_second_throw(self, throw1, throw2):
        if throw2 >= (10-throw1):
            if self.list_of_frame:
                self.second_pre_check(throw1, throw2)
            self.list_of_frame += [["/"]]
            return "/"
        if self.list_of_frame:
            self.second_pre_check(throw1, throw2)
        self.list_of_frame += [[throw1, throw2]]
        return self.list_of_frame[-1]

    def s_frame(self):
        throw1 = self.check_first_throw(
            int(input("Write your hit bowles: "))
        )
        if throw1 == "X":
            print("STRIKE")
            return self.list_of_frame[-1]
        throw2 = self.check_second_throw(
            throw1,
            int(input("Write your next hit bowles: "))
        )
        if throw2 == "/":
            print("SPARE")
        return self.list_of_frame[-1]

    def check_special_special_throws(self):
        if self.list_of_frame[-1][-1] == "X":
            special_throw2 = int(input("Second throw: "))
            special_throw3 = int(input("Third throw: "))
            if special_throw3 <= 10 - special_throw2:
                self.list_of_frame[-1][-1] = 10+special_throw2+special_throw3
            else:
                raise SystemExit("It can't be")  # or print("It can't be")
            self.list_of_frame[-2][-1] = 20+special_throw2
        if self.list_of_frame[-1][-1] == "/":
            special_throw3 = int(input("Third throw: "))
            self.list_of_frame[-1][-1] = 10+special_throw3
        elif self.list_of_frame[-1][-2]+self.list_of_frame[-1][-1] < 10:
            self.list_of_frame[-1] = [self.list_of_frame[-1][-2]+self.list_of_frame[-1][-1]]


count_of_player = int(input("How many player: "))
players = [Player(input(f"Input name player {i+1}: ")) for i in range(count_of_player)]
random.shuffle(players)
print("Turn of players")
for player in players:
    print(player.name)

print("=======")
for i in range(10):
    for player in players:
        print(player.name)
        player.s_frame()
        print(player.list_of_frame)
        print(player.score)
else:
    for i in range(1):
        for player in players:
            print(player.name)
            player.check_special_special_throws()
            print(player.list_of_frame)
            print(player.score)
