# Check a list contains sublist
lst =  [1,2,3,5,6]
sub_lst = [0,5,2]
flag = 0
if(all(x in lst for x in sub_lst)):
    flag = 1
if(flag) == True:
    print("Yes, list is subset of main list.")
else:
    print("No, list is subset of main list.")