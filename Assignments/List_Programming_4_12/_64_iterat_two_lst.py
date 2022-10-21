# Iterate over two lists simultaneously
lst1 = [10,20,30,40,50]
lst2 = [50,60,80,90,100]
for i,j in zip(lst1,lst2):
    print("list one value",i,"and","list two value",j)