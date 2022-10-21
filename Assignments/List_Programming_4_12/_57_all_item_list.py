# Check if all items of a list is equal to a given string
lst = input("Enter your list :").split(',')
first_ele = lst[0]
result = True
for item in lst:
    if first_ele != item:
        result = False
        break
if result == True:
    print("All item of a list is Equal")
else:
    print("All items of a list is not Equal")

