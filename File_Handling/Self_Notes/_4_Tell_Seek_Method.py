'''
tell() Method
-------------
* We can use tell() method to return current position of the cursor from beginning of the file.
* The position of first charater in files is zero just like string index
'''
with open ('doc.txt','r') as f:
    print(f.tell())
    print(f.read(2))
    print(f.tell())
    print(f.read(6))
    print(f.tell())