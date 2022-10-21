# Remove duplicates from a list of lists
def dup_lst(lst):
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    print("Remove duplicates form a list of lists: ",res)
lst = [[1,0],[0,1],[1,1],[2,3],[5,6],[0,1]]
dup_lst(lst)