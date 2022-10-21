# _02_Variables on Program
# An Integers assignment
age = 45
print(age)

# An Integers assignment
salary = 25000.360
print(salary)

# An Srting assignment
emp_name = "Ziba"
print(emp_name)

# declaring a var
Number = 54
# display
print(Number)

print("Before Declaring Variable:",Number)

# re-declare the var
Number = 120
print("After Declaring Variable:", Number)

# ASSIGNING A SINGLE VALUE TO MULTIPLE VARIABLE

a=b=c=10
print(a,b,c)

# ASSIGNING A MULTI VALUE TO MULTIPLE VARIABLE
a , b , c = 10,20,30
print(a,b,c)

# CAN WE USE THE SAME NAME FOR DIFFERENT TYPES
'''If we use the same name, the variable starts referring to a new value and type.'''
b = 10
b = "geeksforgeeks"
print(b)
# OUTPUT
"geeksforgeeks"

# HOW DOES + OPERATOR WORK WITH VARIABLES

A,B = 10,20
print(A+B)

a = "geeksfor"
b = "geek"
print(a+b)

# CAN WE USE + FOR DIFFERENT TYPES ALSO
i,j = 10,"john"
print(i+j)
'''
output
=====
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

# GLOBAL AND LOCAL VARIABLES IN PYTHON
'''
Local variables are the ones that are defined and declared inside the function. we cannot call this variable outside 
the function
'''

def fn():
    # local variable
    s = "python is very easy language"
    print(s)
fn()

# GOBAL VARIABLE
def f():
    print(g)

g = "welcome to MCS"
f()

# OBJECT REFERENCES
x = 6
y = x

