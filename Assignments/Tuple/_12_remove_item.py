#  remove an item from a tuple
num = [10,20,2,3,4,5,3]
n = int(input("Enter the number which num youc remove an item in list: "))
res = []
for i in num:
    if i != n:
        res.append(i)
print("remove an items from a tuple: ",tuple(res))