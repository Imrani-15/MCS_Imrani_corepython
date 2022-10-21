class Muti:
    def __init__(self):
        pass
    def lst_muti(self):
        total = 1
        for ele in range(1,len(lst)):
            total = total*lst[ele]
        print("Multiple the elements in the list:",total)
lst = [1,2,3]
m = Muti()
m.lst_muti()