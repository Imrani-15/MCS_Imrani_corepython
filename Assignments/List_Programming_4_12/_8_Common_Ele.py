# Find common element from 2 lists
class Common:
    def __init__(self):
        pass
    def ele_2_lst(self):
        res = []
        for i in lst1:
            for j in lst2:
                if i == j:
                    res.append(i)
        print("Common Elements from two list:",res)
lst1 = [1,2,3,4,6]
lst2 = [1,2,3,4,5]
c = Common()
c.ele_2_lst()
