# Print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys
d = dict()
for i in range(1,16):
    d[i] = i**2
print(d)