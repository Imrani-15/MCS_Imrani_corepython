#  sum all the numbers in a list
class lst_sum:
    def __init__(self):
        print("This is constructor")
    def adding_lst(self):
        res = 0
        for ele in range(0,len(lst)):
            res = res+lst[ele]
        print("Adding the elements in the list:",res)
lst = [1,2,3,4,5,6]
l = lst_sum()
l.adding_lst()