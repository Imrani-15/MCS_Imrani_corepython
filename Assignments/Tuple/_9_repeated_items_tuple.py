#  find the repeated items of a tuple
num = tuple([10,20,30,50,10,10,50,10])
for i in num:
    if num.count(i)>1:
        print(num.count(i))
        break