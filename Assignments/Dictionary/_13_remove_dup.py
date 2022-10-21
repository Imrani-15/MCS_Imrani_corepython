# Remove duplicates from Dictionary python
my_dict = {'x':500, 'y':5874, 'z': 560,'a':500,'b':560,'c':820}
temp = []
res = dict()
for key,val in my_dict.items():
    if val not in temp:
        temp.append(val)
        res[key] = val
print("Remove duplicates from dictionary: ",res)
