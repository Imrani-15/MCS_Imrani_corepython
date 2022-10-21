# Get the depth of a dictionary python
dict1 = {1: 'Sun', 2: {3: {4:'Mon'}, 6: {7:{5:'Tue'}}}}
count = 0
str_dict1 = str(dict1)
print(str_dict1)
for i in str_dict1:
    if i == "{":
        count = count+1
print("The depth of a dictionary: ",count)

