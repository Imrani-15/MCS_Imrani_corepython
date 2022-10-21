#Mulitply of elements
"By using Build in method"
import numpy
print("==============By using build in method===================")
Multi = [10,20]
result = numpy.prod(Multi)
print("Multiply of elements give a list using build in method",result)

"By using for loop"
print("\n==============By using for loop==========================")
res = 1
for i in Multi:
    res = res*i
print("Multiply of elements give a list using for loop",res)

"By using While loop"
print("\n====================By using while loop=================")
total = 1
ele = 0
while ele<len(Multi):
    total = total*Multi[ele]
    ele = ele+1
print("Multiply of elements give a list using while loop",total)

"By using function"
print("\n================By using function==================")
def multiply(Multi):
    final = 1
    for k in Multi:
        final = final*k
    print("Multiply of elemets give a list using functions",final)
multiply(Multi)

"By using oops concept"
print("\n=================By using oops concept=================")
class Multiply_Ele:
    def __init__(self,Multi):
        self.Multi = Multi
    def pro_ele(self):
        pro = 1
        for n in Multi:
            pro = pro*n
        print("Multiply of elements given a lis using oops concept:",pro)
m = Multiply_Ele(Multi)
m.pro_ele()