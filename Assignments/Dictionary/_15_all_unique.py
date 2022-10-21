# Print all unique values in a dictionary.
dict = {'511':'Vishnu','512':'Vishnu','513':'Ram','514':'Ram','515':'sita'}
lst =[]
for val in dict.values():
  if val in lst:
    continue
  else:
    lst.append(val)

print(lst)