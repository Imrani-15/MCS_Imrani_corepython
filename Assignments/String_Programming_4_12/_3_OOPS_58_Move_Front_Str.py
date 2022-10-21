class Move:
    def __init__(self,str):
        self.str = str
    def front(self):
        char = []
        for ch in str:
            if ch != " ":
                char.append(ch)
#        print(char)
        space = len(str) - len(char)
        print(space)
        result1 = " " * space
        result = result1 + ''.join(char)
        print(result)
str = input("enter your String:")
m = Move(str)
m.front()