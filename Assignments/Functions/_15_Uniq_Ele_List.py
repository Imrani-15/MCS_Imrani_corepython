# takes a list and returns a new list with unique elements of the first list.
class New_List:
    def __init__(self):
        pass
    def unique_ele(self):
        res = []
        for ele in lst:
            if ele not in res:
                res.append(ele)
        print(res)
lst = input("Enter your list:").split(",")
n = New_List()
n.unique_ele()