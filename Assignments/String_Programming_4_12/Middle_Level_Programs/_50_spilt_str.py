# split a string on the last occurrence of the delimiter
txt = input("Enter the string with separations(like , or - ) :")
n = int(input("Enter the the number split a string on the last occur: "))
print(txt)
res = txt.rsplit(' ',n)
print("The splitted list at the last comma :",(res))
