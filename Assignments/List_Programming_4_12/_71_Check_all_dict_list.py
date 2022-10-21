# Check if all dictionaries in a list are empty or not
lst1 = [{},{},{}]
all_empty = True
for i in lst1:
    if i:
        all_empty = False
print(all_empty)
