# convert a tuple to a string
num = tuple([10,20,30,40,50,60,70])
str1 = " "
for i in str(num):
    str1 = str1+i
print("Convert a tuple to a string: ",str1)
print(type(str1))