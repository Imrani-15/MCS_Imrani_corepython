# Remove an item from a set if it is present in the set.
def remove_item(set1):
    set1.discard(pre_item)
    print(set1)
set1 = set([10,20,30,50,40,20,10,52,62])
pre_item = int(input("Enter your number:"))
remove_item(set1)