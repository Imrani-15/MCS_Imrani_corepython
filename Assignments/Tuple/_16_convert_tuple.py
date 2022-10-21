# convert a tuple to a dictionary
tup1 = (1,2,3,4)
tup2 = ('ram','ravi','sitha','kunal')
if len(tup1) == len(tup2):
    res = dict(zip(tup1,tup2))
    print("Conver a tuple to a dictionary: ",res)