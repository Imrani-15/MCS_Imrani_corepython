# Extend a list without append python
def lst_without_app(lst1,lst2):
    res  = lst1+lst2
    print("Extend a list without append: ",res)
lst1 = input("Enter your list: ").split(",")
lst2 = input("Enter your list: ").split(",")
lst_without_app(lst1,lst2)