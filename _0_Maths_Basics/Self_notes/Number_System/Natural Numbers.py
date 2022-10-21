# Programming on Natural Numbers
# print 1 to n natural numbers
# using for loop
print("=================Natural Numbers using For loop====================")
n = int(input("Enter Maximum numbers:"))
print("Natural number 1 to ",n)
for i in range(1, n+1):
    print(i)

# # print 1 to n natural numbers using while loop
print("=========Natural Numbers using While loop============")
num = int(input("Enter Maximum numbers:"))
print("Natural number 1 to",num)
i = 1
while i<=num:
    print(i)
    i+=1
#
# # Print 1 to n natural numbers using functions
print("=======Natural Numbers using Functions=============")
num1 = int(input("Enter Maximum numbers:"))
print("Natural numbers 1 to ",num1)
def show_natural(num1):
    for i in range(1,num1+1):
        print(i)
show_natural(num1)

# write a progarm print even numbers
# using for loop
print("=====================Even Numbers using For loop======================")
for num in range(10):
    if num%2==0:
        print(num,end=" "'\n')

# write a program print even numbers
# using while loop
print("===========================Even numbers using While loop=============================")
num = 2
while num<=20:
    if num%2==0:
        print(num,end=" ")
    num+=1

