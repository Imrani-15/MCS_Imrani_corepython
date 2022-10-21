# python Clone or copy
class Clone:
    def __init__(self):
        pass
    def copy_clone(self):
        lst_copy = []
        lst_copy.extend(lst)
        print(lst_copy)
lst = [12,20,30,14,52,62]
lst1 = lst
print("after cloning",lst1)
c = Clone()
c.copy_clone()


