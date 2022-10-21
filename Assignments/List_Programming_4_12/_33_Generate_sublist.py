# Generate all sublists

def sub_list(lst):
    lists = [[]]
    for i in range(len(lst)+1): #[1,2,3]
        for j in range(i):
            lists.append(lst[j: i])
    return lists
lst= [1,2,3]
print(sub_list(lst))