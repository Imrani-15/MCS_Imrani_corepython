#form itertools import combinations
input_str_array = input("Enter the integers:").split(",")
integers = []

'''    if item.isalpha():
#        print("plz enter the proper intergers")
#    break'''

# n = int(input("enter the intergers:")
# for i in range(n):
for item in input_str_array:
#    for subitem in item.split():
    if item.isdigit():
        integers.append(int(item))
print(integers)
#lst_tuple = [x for x in zip(*[iter(integers)]*2)]
#print(lst_tuple)
# input = [(1,2),(3,4)]
# output = [(1,3),(1,4),(2,3),(2,4)]
result = []
for i in integers:
    for j in integers:
        if (i+j==7):
            tup = tuple(sorted([i,j]))
            if tup not in result:
                result.append(tup)
print(result)



#lst_tuple = [x for x in zip(*[iter(integers)]*2)]
#print(lst_tuple)
