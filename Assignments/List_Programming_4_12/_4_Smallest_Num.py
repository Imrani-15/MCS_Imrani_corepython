# Smallest number from list
class Smallest:
    def __init__(self,list):
        self.list = list
    def chota(self):
        small = list[0]
        for i in list:
            if i< small:
                small = i
        print("Smallest number from the list:",small)
list = [0,10,20,0,1]
s = Smallest(list)
s.chota()
