# create a dictionary from two lists without losing duplicate values.
lst_one = ['one','two','three','four','five']
lst_two = [10,20,30,40,50]
dict_1={}
for key,value in zip(lst_one,lst_two):
    if key not in dict_1:
        dict_1[key]=value
    else:
        dict_1[key].append(value)

print(dict_1)
