import random
class Shu_List:
    def __init__(self):
        print("This is Constructor:")
    def change_list(self):
        for i in range(len(lst)-1,0,-1):
            j = random.randint(0,i+1)
            lst[i],lst[j] = lst[j], lst[i]
        print("After Shuffle the list:",lst)
lst = [1,2,3,4,5,6]
print("Original list before shuffle:",lst)
s = Shu_List()
s.change_list()