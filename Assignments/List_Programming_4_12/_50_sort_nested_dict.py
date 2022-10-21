# Sort a list of nested dictionaries
from  operator import itemgetter
'''
that is just what operator.itemgetter(1) will give you: A function that grabs the first item from a list-like object.
itemgetter is tearted as in dict get[key] method
'''
lst_dict1 = [
    {'name':'kevin','age':35},
    {'name':'johny','age':63},
    {'name':'kottiga','age':96},
    {'name':'ramanaidu','age':52}
]
lst_dict1.sort(key=itemgetter('name'))
print(lst_dict1)