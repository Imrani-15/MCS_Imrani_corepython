# print the following integers with zeros on the left of specified width
x = int(input("Enter your Number:"))
print("Original Number:",x)
print("Integers with zeros on the left of specified width :" + "{:0>3d}".format(x))