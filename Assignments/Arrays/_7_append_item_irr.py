# Append items from inerrable to the end of the array
from array import *
arra_num = array('i',[1, 3, 5, 7, 9])
print("Original array: "+str(arra_num))
arra_num.extend(arra_num)
print("Extend array: "+str(arra_num))