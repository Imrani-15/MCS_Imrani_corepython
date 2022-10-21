# Get the current memory address and the length in elements of the buffer used to hold an arrays? contents and also find the size
import numpy as np
x = np.array([100,20,34])
print("size of array: ",x.size)
print("Memory size of a Numpy array: ",x.nbytes)