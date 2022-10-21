# Get the top three items in a shop.
from  heapq import nlargest
from operator import itemgetter
my_dict = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for name,value in nlargest(3,my_dict.items(),key=itemgetter(1)):
    print("The top three items in a dict: ",name,value)