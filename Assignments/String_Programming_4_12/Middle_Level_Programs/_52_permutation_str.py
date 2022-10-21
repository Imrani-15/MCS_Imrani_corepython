# print all permutations with given repetition number of given string
def permute(str1,res):
    if (len(str1) == 0):
        print(res,end=" ")
        return 0
    for i in range(len(str1)):
        char1 = str1[i]
        left_sub = str1[0:i]
        right_sub = str1[i+1:]
        final_res = left_sub+right_sub
        permute(final_res,res+char1)
res = ""
str1 = input("Enter your string: ")
print("All possible string are: ")
permute(str1,res)
