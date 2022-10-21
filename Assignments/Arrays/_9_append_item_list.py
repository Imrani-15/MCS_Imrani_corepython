# Append items from a specified list.
from array import *
num_list = [1, 2, 6, -8]
array_num = array('i',[])
print("Item in the list: "+str(num_list))
print("Append items from the list: ")
array_num.fromlist(num_list)
print("Item in the array: "+str(array_num))