# Remove odd index values
class Odd:
    def __init__(self,str):
        self.str = str
    def index(self):
        res = ""
        for i in range(len(str)):
            if i%2!=0:
                res = res+str[i]
        print(res)
str = input("enter your string:")
o = Odd(str)
o.index()

