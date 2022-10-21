# Printing elements in ascending order
lst = [5,2,8,3,1]
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print("Sorted list is: ",lst)