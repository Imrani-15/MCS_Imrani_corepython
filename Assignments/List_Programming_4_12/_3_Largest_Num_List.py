"Largest number of the list"
print("====largest number of the list by using build in method====")
list = [100,20,30,15,200]
max1 = max(list)
print("Largest number of the list:",max1)

print("\n====largest number of the list by using for loop====")
largest = list[0]
for i in list:
    if i>largest:
        largest = i
print("Largest number of the list by using for loop",largest)

print("\n====largest number of the list by using while loop===")
x = 0
lar = list[x]
while x<len(list):
    if list[x]>lar:
        lar = list[x]
    x = x+1
print("Largest number of the list by using while loop:",lar)

print("\n====Largest number of the list by using functions====")
def largest(list):
    list1 = []
    for j in list:
        list1.append(j)
    list1.sort()
    print("Largest number if the list by using functions:",list1[-1])
largest(list)

print("\n====Largest number of the list by using oops concept====")
class Big_Num:
    def __init__(self,num):
        self.num = num
    def large(self):
        list2 = []
        for k in range(1,num+1):
            ele = int(input("enter elements:"))
            list2.append(ele)
        print("lagest number is:", max(list2))
num = int(input("enter number of elements in list: "))
b = Big_Num(num)
b.large()
