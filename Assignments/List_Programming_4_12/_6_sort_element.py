lst = [5, 2, 8, 7, 1, 3, 13, 64, 23, 15, 48, 39, 9]
temp = 0
print("Elements of Original list:")
for i in range(0,len(lst)):
    print(lst[i],end=" ")

for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
print()
print("Element of array sorted in asending order:")
for i in range(0,len(lst)):
    print(lst[i],end=" ")



