# All permutations of list elements
import itertools

lst1 = [1,2,3,4]
permutation_obj = itertools.permutations(lst1)
permutation_lst = list(permutation_obj)
print("Permutations of list elemets: ",permutation_lst)