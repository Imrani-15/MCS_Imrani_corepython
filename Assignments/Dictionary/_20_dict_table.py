# Print a dictionary in table format.
dict1 = {"python":20,"django":30,"mangodb":25}

print("SubName",'\t',"Quntity")
for i,j in dict1.items():
    print(i,'\t',j)