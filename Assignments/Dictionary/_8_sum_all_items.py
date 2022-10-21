# Sum all the items in a dictionary
def all_items(mydict):
    lst = []
    for i in mydict:
        print(mydict[i])
        lst.append(mydict[i])
    final = sum(lst)
    return final

mydict = {'a': 100, 'b':200, 'c':300}
print("Sum: ",all_items(mydict))
