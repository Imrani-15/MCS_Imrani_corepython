str = '12,23,45,2.12.15,63.'
dict = {".":",",",":"."}
#print(dict)
s = str.maketrans(dict)
print(s)
final = str.translate(s)
print(final)

