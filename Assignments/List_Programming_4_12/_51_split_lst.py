# Split a list every Nth element
def spli_n_ele(lst,n):
    return [lst[i::n] for i in range(n)]

lst = [1,2,3,4,5,6,4,5,6,8,7,6,10,25,0]
n = int(input("Enter your number:"))
print(spli_n_ele(lst,n))
