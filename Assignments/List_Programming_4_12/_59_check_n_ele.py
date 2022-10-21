# Check if the n-th element exists in a given list
def n_ele_exit(lst):
    for i in lst:
        if i == n:
            print("Element Exists")
    print("{}".format(n), "Element exitst in a give list")

lst = input("Enter the list here: ").split(",")
n = int(input("Enter the number here and element exist in a given list:"))
n_ele_exit(lst)
