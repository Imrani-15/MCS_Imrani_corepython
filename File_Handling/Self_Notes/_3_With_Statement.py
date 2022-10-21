'''
THE WITH STATEMENT
-----------------
1 The with statement can be used while opending a file. We can use this to group file operation
   statements within block
2 The advantage of with statement file is take care closing of file, after completing all operation
   automatically
'''
with open('doc.txt','w') as f:
    f.write("MCS\n")
    f.write("software solutions\n")
    f.write("Private Limited\n")
print("Is file closed",f.closed)

