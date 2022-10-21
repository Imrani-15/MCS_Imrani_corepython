# Remove even elements and print list
class Remove_Even:
    def __init__(self):
        print("This is constructor")
    def even_ele(self):
        res = []
        for ele in lst:
            if ele%2!=0:
                res.append(ele)
        print(res)
lst = [2,3,4,5,6,7,8,9,10,12]
r = Remove_Even()
r.even_ele()