# First last chars swappingFirst last chars swapping
class Swap_first_Last:
    def __init__(self,str):
        self.str = str
    def swap(self):
        start = str[0]
        end = str[-1]
        swap_str = end+str[1:-1]+start
        print(swap_str)
str = input("Enter your string:")
s = Swap_first_Last(str)
s.swap()
