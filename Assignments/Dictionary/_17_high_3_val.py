# find the highest 3 values in a dictionary python
from operator import itemgetter
from itertools import islice

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5875, 'f': 20}
new_list = sorted(my_dict.values())
print("Sorted the dictionary: ",new_list)
print("The highest 3 values in a dictionary: ",new_list[-3:])
