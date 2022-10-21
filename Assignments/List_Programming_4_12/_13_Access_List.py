# To access index of list
class Access:
    def __init__(self):
        print("This is consturctor:")
    def access_list(self):
        print("Print List of Index Values are:")
        for i in range(len(lst)):
            print(i,end="-")
            print(lst[i])
lst = [12,3,45,10,30,41]
a = Access()
a.access_list()