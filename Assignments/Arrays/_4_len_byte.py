# Get the length in bytes of one array item in the internal representation.
import numpy as np
array = np.array([1,3,5,6], dtype=np.float64)
# size of the array
print(array.size)
# length of one array element in bytes
print(array.itemsize)
# Total bytes consumed by the element of the array
print(array.nbytes)

