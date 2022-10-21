# Convert a string to a list
str1 = input("Enter your string here: ")
res = []
for i in str1.split(" "):
    print(i)
    res.append(i)
print(res)