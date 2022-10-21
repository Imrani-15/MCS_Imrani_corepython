# Change the position of every nth value with (n+1)th value
# from itertools import zip_longest, chain, tee
# def replace_copy(n):
#     lst1, lst2 = tee(iter(n), 2)
#     return list(chain.from_iterable(zip_longest(n[1::2], n[::2])))
# n = [0,1,2,3,4,5]
# print(replace_copy(n))

lst = [1,2,4,5,6,7]
for i in range(0,len(lst),2):
    lst[i],lst[i+1] = lst[i+1],lst[i]
print(lst)


