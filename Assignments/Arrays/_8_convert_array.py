# Convert an array to an array of machine values and return the bytes representation
from array import *
print("Bytes to String: ")
x = array('b', [114,  111, 119 ])
s = x.tobytes()
print(s)
