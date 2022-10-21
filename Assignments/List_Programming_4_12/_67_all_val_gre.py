# Find all the values in a list are greater than a specified number
def val_check(lst1,val):
    for i in lst1:
        if val >= int(i):
            return False
    return True

lst1 = input("Enter your list here: ").split(",")
val = int(input("Enter your number: "))
if(val_check(lst1,val)):
    print("Yes")
else:
    print("No")