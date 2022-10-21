# Convert list to list of dictionaries
lst = ['pavani',50,'karthick',80,'johny',50,'ziba',100]
key_value = ['name','marks']
res = []
n = len(lst)
for i in range(0,n,2):
    res.append({key_value[0]:lst[i],key_value[1]:lst[i+1]})
print(res)
