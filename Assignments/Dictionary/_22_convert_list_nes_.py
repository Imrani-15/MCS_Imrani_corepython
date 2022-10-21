# Convert a list into a nested dictionary of keys.
test_list1 = ["ravi", 'ram', 'johny']
test_list2 = ['kotti', 'dhana', 'karry']
test_list3 = [60, 50, 10]
res  = [{a:{b:c}} for (a,b,c) in zip(test_list1,test_list2,test_list3)]
print("convert a list into a nested dict: ",res)