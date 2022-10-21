# 4 Copies of last 2 chars
class Four_copies:
    def __init__(self):
        pass
    def last_char(self):
        res = txt[-2:]
        print("Four copies of last 2 char:",res*4)

txt = input("Enter your string:")
f = Four_copies()
f.last_char()