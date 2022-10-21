# Get the maximum and minimum value in a dictionary.
my_dict = {'x':500, 'y':5874, 'z': 560}
key_max = max(my_dict,key=my_dict.get)
key_min = min(my_dict,key=my_dict.get)
print("Minimum key in dictionary: ",key_min)
print("Maximum key in a dictionary: ",key_max)
val_max = max(my_dict.values())
val_min = min(my_dict.values())
print("Minimum value in a dictionary: ",val_min)
print("Maximum value in a dictionary: ",val_max)