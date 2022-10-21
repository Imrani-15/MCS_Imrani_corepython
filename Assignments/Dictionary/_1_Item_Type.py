# Prints each item and its corresponding type from the following list.
class Item_Type:
    def __init__(self,list):
        self.list = list
    def find(self):
        for i in list:
            print("Item of",i,"type of",type(i))
list = [1452, 11.23, 1+2j, True, 'mango', (0, -1), [5, 12], {"class":'V', "section":'A'}]
i = Item_Type(list)
i.find()