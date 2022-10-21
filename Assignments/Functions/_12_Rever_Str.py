class Rever_str:
    def __init__(self):
        pass
    def back_word(self):
        res = ""
        for char in str:
            res = char+res
        print("Reverse string is :",res) #print(str[::-1]
str = input("enter your string:")
r = Rever_str()
r.back_word()