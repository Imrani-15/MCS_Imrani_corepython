
# print(len(str))
# print(str[0:6])
# print(str[::-1])
# print(str[1:-1])
# print(str[0:16:2])
# print(str[0:60:4])
# s3 = slice(-1,-16,-3) #using the slice constructor
# print(str[s3])
# s4 = slice(-1,-15,-2)
# print(str[s4])
# s5 = slice(-6)
# print(str[s5])

class String:
    def __init__(self,str):
        self.str = str
    def func(self):
        result =self.str[0:4]
        print(result)
str = "you can start installing or using packages in your virtual environment you’ll need to activate it"
s = String(str)
s.func()