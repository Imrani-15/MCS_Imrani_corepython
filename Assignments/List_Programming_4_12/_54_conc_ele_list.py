# Concatenate elements of a list
def concat_ele(lst1,lst2):
    for i in lst2:
        lst1.append(i)
    print(lst1)
lst1 = [1,2,3,5,4,6]
lst2 = [10,20,30,40,50]
concat_ele(lst1,lst2)