# Finding common items from two lists
def common_item(one,two):
    res = []
    for lst1,lst2 in zip(one,two):
        if lst1 == lst2:
            res.append(lst1)
    print("Common items from two list:", res)



one = [1,2,3,4]
two = [5,6,7,8]
common_item(one,two)