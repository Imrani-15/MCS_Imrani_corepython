# Compute the similarity between two lists
def two_lst(lst1,lst2):
    lst1.sort()
    lst2.sort()
    if lst1 == lst2:
        print("Two list are Equal")
    else:
        print("Two list are not equal")
lst1 = [1,5,3,2]
lst2 = [1,2,3]
two_lst(lst1,lst2)