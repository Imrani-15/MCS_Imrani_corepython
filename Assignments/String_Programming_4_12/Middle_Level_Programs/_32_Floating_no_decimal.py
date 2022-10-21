# print the following floating numbers with no decimal places
x = float(input("Enter First Number: "))
y = float(input("Enter Second Number: "))
print("Original Number:",x)
print("Floating number with no decimal places:" + "{:.0f}".format(x))
print("Floating number with no decimal places:" + "{:.0f}".format(y))