# Get unique values
def get_unique(lst):
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    print(res)
lst = [10,10,20,50,10,20,30,50,60]
get_unique(lst)