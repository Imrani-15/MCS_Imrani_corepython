# Converting multiple integers into single integer
def conver(lst):
    res = [str(i) for i in lst]
    final = int("".join(res))
    return final
lst = [1,2,3,4,5]
print("Convrting multiple integers into sibgle interger: ",conver(lst))
