# Find missing and additional values
lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [4, 5, 6, 7, 8]
# prints the missing and additional elements in list2
print("Missing value in second list:",(set(lst1).difference(lst2)))
print("Additional value in second list:",(set(lst2).difference(lst1)))

# prints the missing and additional elements in list1
print("Missing value in first list: ",(set(lst2).difference(lst1)))
print("Additional value in first list: ",(set(lst1).difference(lst2)))