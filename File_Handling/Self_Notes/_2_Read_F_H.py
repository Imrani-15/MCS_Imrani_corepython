'''read() this method total data from the file
read(n) this method 'n' charater data from the file
readline() this method only one line data from the file
readlines() this method all lines data from the file
'''
f = open('doc.txt','r')
# result = f.read()
# print(result)
# final = f.read(10)
# print(final)
# line = f.readline()
# print(line)
lines = f.readlines()
for line in lines:
    print(line,end="")
f.close()