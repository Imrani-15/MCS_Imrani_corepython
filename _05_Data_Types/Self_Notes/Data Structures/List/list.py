# create of list objects
# create a empty list object as follows
lst = []
print(lst)
print(type(lst))

# if we know already then we can create list as follows list = [10,20,30,40]

# with dynamic input means take input from the user
lst1 = eval(input("enter the list here:"))
print(lst1)
print(type(lst1))

# With list function
res  = list(range(10))
print(res)
print(type(res))

srt = list(input("enter the string here"))
print(srt)
print(type(srt))

# with split() function

s = input("enter the string here:").split(",")
print(s)
print(type(s))

# By using slicing operator
n = [1,2,3,4,5,6,7,8,9,10,11]
print(n[0:7:2])
print(n[4:10])
print(n[0:4:3])
print(n[::-1])
print(n[0:5:-1])
print(n[5:100])

# List vs Mutability
# Once we create a list we can modify its content. Hence list is mutable
b = [10,20,30,40]
b[1] = 25  # we can modify the list object here
print(b)

# Traversing the element of list
'''The sequential access of each element in the list is called traversal'''
# By using while loop

n = [1,2,3,4,5,6,7,8,9]
i = 0
while i<len(n):
    print(n[i])
    i = i+1
# By using for loop

n1 = [1,2,3,4,5,6,7,8,9]
for i in n1:
    print(i)

# To Display even numbers using for loop
for i in range(10):
    if i%2==0:
        print(i)
#To Display even numbers using while loop
n = int(input("Enter ur number: "))
i = 1
while i<n:
    if i%2==0:
        print(i)
    i = i+1

# To diplay Element by index wise
a = ['a','b','c']
x = len(a)
for i in range(x):
    print(a[i],"is avaliable at positive index:",i,"and nagetive index:",i-x)

# To get information about list:
#1. len()
'''Return the number of element present in the list'''
l = [10,20,30,40]
print(len(l)) # 4

#2.Count()
'''Return the number of occurrence of specified item in the list'''

n = [1,1,1,1,1,2,2,2]
print(n.count(1))
print(n.count(2))

#3.Index()
'''Return the index of first occurence of the specified item'''
n = [1,1,1,1,1,2,2,2]
print(n.index(1))
print(n.index(2))

# Manipulating Elements in the list:
# 1. append() function
'''we can use append() function to add item at the end of the list'''
ls = []
ls.append(10)
ls.append('A')
ls.append(50)
print(ls)

# To add all element to list upto 100 which are divisiable by 10
lst = []
for i in range(101):
    if i % 10==0:
        lst.append(i)
print(lst)


# insert() function
'''To insert item at specific index position'''
n = [1,2,3,5,4]
print(n.insert(1,20))
print(n)

n = [1,2,3,4,5,6]
print(n.insert(10,200))
print(n.insert(-10,300))
print(n) # output [300,1,2,3,4,5,6,200]

'''Note: If the specified index is greater then max index then element will be insert at last
position. If the specifed index is smaller than min index then element will be inserted at the
first position'''

# extend() function
'''To add all items of one list to another list
l1.extend(l2)
print(l1)
all items present in l2 will be added in l1
'''
order1 = ['Chicken','Mutton','Fish']
order2 = ['RC','KF','FO']
order1.extend(order2)
print(order1)

order = ['Chicken','Mutton','Fish']
order.extend('Mushroom')
print(order)

# Remove() function
'''We can use this function to remove specified item from the list. If the item present multiple
times then only first occurence will be removed'''
# Note: If the specified item not present in list then we will get ValueError
# Hence before using remove() method first we have to check specified element present in the
# list or not by using in operator

n = [10,20,30,40,10]
n.remove(10)
print(n)

# Pop() function
'''
1. It removes and returns the last element of the list
2. this is only function which manipulates list and return some element
'''
n1 = [10,20,3,40,20,10]
print(n1.pop())
print(n1.pop())
print(n1)
# Note: If the list is empty then pop() function raises IndexError
s = []
print(s.pop())
'''
In general we can use pop() function to remove last element of the list. But we can use to
remove element based on index
'''
# n.pop(index)  To remove and return element present at specified index
# n.pop() to remove and return last element of the list

n = [10,20,30,40,50,60,50]
print(n.pop()) # 50
print(n.pop(1)) # 20
print(n.pop(10)) # IndexError: POP index out of range

'''
append()/insert()/extend() for incresing the size
remove()/pop() for decreasing the size
'''

# Ordering Element of lists:

#1. reverse()
'''
We can use to reverse() order of  element of the list
'''
# program 1
n = [10,20,30,40]
print(n.reverse())
print(n)

# Program 2
for i in reversed(n):
    print(i,end=" ")

#2. Sort()

'''
In list by default insertion order is preserved. If you want to sort the element of list
according to default natural sorting order then we should go for sort() method
For number ==> Default Natural sorting order is Acending order
For String ==> Default natural sorting order is Alphabetical order
'''
n = [20,0,1,3,2]
n.sort()
print(n) # [0,1,2,3,20]

s = ['Dog','Banana','Cat','Apple']
s.sort()
print(s) # ['Apple','Banana','Cat','Dog']

n = int(input("Enter the number here: "))
ls = []
for i in range(n):
    if i%10 == 0:
        ls.append(i)
print(ls)
ls.sort(reverse=True)
print(ls)

# Note: To use sort() function, compulsory list contain only homogeneous elements. otherwise
# we will get error

n = [50,"A","B",10]
n.sort()
print(n)

'''
TypeError: '<' not supported between instances of 'str' and 'int'

Note: In Python 2 if List contains both numbers and Strings then sort() function first sort 
numbers followed by strings
1) n=[20,"B",10,"A"] 
2) n.sort() 
3) print(n)# [10,20,'A','B'] 

But python 3 it is invalid
'''
# Aliasing and cloning of list objects:

'''
The process of giving another reference variable to the existing list is called aliasing 
'''

x = [10,20,30,40,50]
y = x
y[1] = 70
print(x)
'''
The problem in this approach is by using one reference variable if we are changing content, then
those changes will be reflected to the other reference variable

To over come this problem we should go for cloning

The process of creating exactly duplicate independent object is called cloning 

We can implement cloning by using slice operator or using copy() function
'''

# By Using Slice Operator:
x = [10,20,30,40,70]
y = x[:]
y[1] = 50
print(x) # [10,20,30,40,70]
print(y) # [10,50,30,40,70]

# By using copy() Function

x = [10,20,30,40,70]
y = x.copy()
y[2] = 100
print(x)
print(y)

# Different between = operator and copy() Function
# 1. =operator meant for aliasing
# 2. copy() Function meant for cloning


# Using Mathematical Operators for list Object
'''We can use  + and * operators for list object'''
#1. Concatenation operation(+)

a = [10,20,30]
b = [50,60,70]
c = a+b
print(c)
'''
Note: To use + operator compulsory both arguments should be list object otherwise we will get 
TypeError
'''

# 2. Repetition Operator (*) :
x = [10,20,30]
y = x*3
print(y)

# Comparing List Objects
'''
We can use comparison operators for list object

Note: Whenever we are using comparison operators (==,!=) for list objects then the following 
should be considered

1. The number of Element
2. The order of Element
3. The content of Element (case Sensitive)
'''

x = ['Dog',"Cat","Rat"]
y = ["Dog","Cat","Rat"]
z = ["dog","cat","rat"]
print(x==y) # True
print(y==z) #False
print(x!=z) # True





