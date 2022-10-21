#  find the maximum occurring character in a given string
txt_str  = input("Enter your string: ")
res  = {}
for i in txt_str:
    if i in res:
        res[i]  = res[i]+1
        print(res)
    else:
        res[i] = 1
final = max(res,key=res.get)
print(final)