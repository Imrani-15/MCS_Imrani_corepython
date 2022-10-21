'''
x = raw_input("Enter First Number")
print(type(x))
It will always print str type only for any input type ===> python 2.0 version
'''

# Input
x = input("Enter value:")
print(x)

# write a program to read 2 numbers from the keyboard and print sum
# First Method
x = input("Enter first Number:")
y = input("Enter Second Number:")
i = int(x)
j = int(y)
print("The sum:",i+j)

# second Method
x = int(input("Enter First number:"))
y = int(input("Enter Second Number:"))
print("The sum:",x+y)

# Third Method
a,b = [int(x)for x in input("Enter Two numbers at a time:").split()]
print("Product is:",a*b)

#Fourth Method
a,b,c = [float(x)for x in input("Enter 3 numbers:").split(",")]
print("The sum:",a+b+c)

# eval Function take a string and evaluate the result
x = eval(input("Enter Expression:"))
print(x)

# Output statement
'''
We can use print() function to display output
'''

#Form1
# Without any argument just it print new line character
print()

#Form2
print("string")
print("Hello World")
# We can use escape characters also
print("hello \n world")
print("Hello \t World")
# We can use repetetion operator (*) in the string
print(10*"Hello")
print("Hello"*10)
# we can use + operator also
print("Hello"+"World")
print("Hello","World")

#Form3
a,b,c = 10,20,30
print("The value are:",a,b,c)

#Form4
# print() with end attribute
print("Hello",end="")
print("World",end="")
print("Name")


