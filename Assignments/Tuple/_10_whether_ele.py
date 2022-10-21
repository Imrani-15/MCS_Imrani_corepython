# check whether an element exists within a tuple
t = input("Enter the tuple here: ")
a = tuple(int(x) for x in t.split(","))
print(a)
ele = int(input("Enter the element here: "))
if ele in a:
    print(ele,"Exists within a tuple")
else:
    print(ele,"Does not exists in tuple")