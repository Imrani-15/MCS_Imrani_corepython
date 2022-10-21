# Multiply all the items in a dictionary
def all_multi(mydict):
    item = 1
    for i in mydict:
        item = item*mydict[i]
    print("Multiply all the items in the dictionary:",item)
mydict = d = {'a': 10, 'b': 7, 'c': 2}
all_multi(mydict)