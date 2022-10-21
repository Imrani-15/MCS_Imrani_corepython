# Insert a given string at the beginning of all items in a list
num = input("Enter the list here: ").split(",")
#ins_str = input("Enter your string here: ")
print(["python {0}".format(i) for i in num])
print()