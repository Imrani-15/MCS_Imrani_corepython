# Create and display all combinations of letters, selecting each letter from a different key in a dictionary
import itertools
my_dict = {'a':2,'b':1,'c':5}
print("Original dictionary: ",my_dict)
res = list(itertools.combinations(my_dict,2))
print("All combinations keys: ",res)