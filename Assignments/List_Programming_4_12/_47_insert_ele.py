# Insert an element before each element of a list
number = [10,20,30,50]
print("Original List:",number)
number = [i for ele in number for i in (70,ele)]
print("Insert an element before each element of a list:",number)