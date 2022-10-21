# s=input("Enter Some String:")
# l=s.split()
# l1=[]
# i=0
# while i<len(l):
#     l1.append(l[i][::-1])
#     i=i+1
#     output=' '.join(l1)
# print(output)

# from functools import reduce
# lst = [1,1,1,1,2,2,2,3,3,3]
# one = []
# two = []
# third = []
# for i in lst:
#     if i == 1:
#         one.append(i)
#     elif i == 2:
#         two.append(i)
#     elif i == 3:
#         third.append(i)
# result = reduce((lambda x,y:x*y),one)
# result1 = reduce((lambda x,y:x*y),two)
# result2 = reduce((lambda x,y:x*y),third)
# print(result+result1+result2)
# print(result1)
# print(result2)

str="0000000092000.000000166.0000000/24"
res=str.split(".")
lst=[]
for i in res:
    a=i.lstrip("0")
    if a[0]!="/":
        lst.append(a)
    elif a[0]=="/":
        print("mask is:",a[1::])

str2=".".join(lst)
print("ip is",str2)