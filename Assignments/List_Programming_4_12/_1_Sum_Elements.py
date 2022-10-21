"By using the Build in method"
print("================By using the build in method===================")
list = [10,20,30,40]
result = sum(list)
print("sum of the elements in given list:",result)

"By using the for loop"
print('\n========================= By using the for loop===============')
res = 0
for i in list:
        res = res+i
print("sum of the elements in given list:",res)

"By using the while loop"
print('\n================By using the while loop====================')
total = 0
ele = 0
while ele<len(list):
    total = total+list[ele]
    ele = ele+1
print("sum of the elements in given list:",total)

"sum of the elements in given list by using the functions: "
print("\n===================By using the function==============")
def sum_list(list):
    sum_list = 0
    for i in list:
        sum_list+=i
    return sum_list
print("sum of the elements in given list:",sum_list(list))

"sum of the elements in given list by using the oops concept"
print("\n===============By using the oops concept=================")
class Sum:
    def __init__(self,list):
        self.list = list
    def sum_ele(self):
        sum = 0
        for j in list:
            sum = sum+j
        print("Sum of the element in given list using oops concept:",sum)
s = Sum(list)
s.sum_ele()

