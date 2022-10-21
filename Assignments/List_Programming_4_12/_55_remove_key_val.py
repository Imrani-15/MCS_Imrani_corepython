# Remove key values pairs from a list of dictionaries
lst_dict = [{"id" : 1, "data" : "Happy"},
             {"id" : 2, "data" : "coding"},
             {"id" : 3, "data" : "guys"}]
for i in range(len(lst_dict)):
    if lst_dict[i]['id'] == 3:
        del lst_dict[i]
        break
print("Remove key Values pairs from a list of dictionaries: ",lst_dict)
