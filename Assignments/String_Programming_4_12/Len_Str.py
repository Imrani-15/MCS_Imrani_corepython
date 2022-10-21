# Find Length of the string by using len build in function
str = "This is MCS Software company"
print("Find Length of the string by using len build in function",len(str))

# Find Length of the string by using for loop
print("\n================USING FOR LOOP=========================")
n = 0
for i in str:
    n = n+1
print("Find the length of string by using for loop:",n)

# Find length of the string by using while loop
print("\n=====================USING WHILE LOOP==================")
N = 0
while str[N:]:
    N = N+1
print("Find the length of string by using while loop:",N)

# Find length of the string by using functions

print("\n===========================USING FUNCTIONS===============")
def str_len(name):
    tot = 0
    for res in name:
        tot = tot+1
    print(tot)
name = input("enter the String:")
str_len(name)

print("\n=================USING LAMBDA FUNCTION===============")
x = (lambda str: len(str))
print(x)
