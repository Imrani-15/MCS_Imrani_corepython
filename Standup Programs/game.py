class Game(object):
    one_player = []
    two_player = []
    def __init__(self):
        pass
    def player_one(self):
        vowels = "aeiouAEIOU"
        res = [txt[i: j] for i in range(len(txt))
               for j in range(i + 1, len(txt) + 1)]
        for char in res:
            if char[0] in vowels:
                Game.one_player.append(char)
        print("Player one charaters from the string:",Game.one_player)
    def player_two(self):
        vowels = "aeiouAEIOU"
        res = [txt[i: j] for i in range(len(txt))
               for j in range(i + 1, len(txt) + 1)]
        for two in res:
            if two[0] not in vowels:
                Game.two_player.append(two)
        print("Player two charater from the string:",Game.two_player)
    def result(self,one_player,two_player):
        self.one_player = one_player
        self.two_player = two_player
        if len(one_player)>len(two_player):
            print("Player one is Winner")
        elif len(one_player) == len(two_player):
            print("Game is Tie")
        else:
            print("Player Two is Winner")
txt = input("Enter The String:")
g = Game()
g.player_one()
g.player_two()
g.result(Game.one_player,Game.two_player)


