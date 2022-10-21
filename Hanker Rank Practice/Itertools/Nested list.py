'''
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names
alphabetically and print each name on a new line.
Example:
records = [["chi",20.0],["beta",50.0],["alpha',50.0]]
The ordered list of scores is [20.0,50.0] , so the second lowest score is 50.0 .
 There are two students with that score:["beta","alpha"] .
Ordered alphabetically, the names are printed as:

alpha
beta
'''

lis = []
n = int(input("Enter the number here:"))
for _ in range(n):
    name = input("Enter the names here: ")
    score = float(input("Enter the score here: "))
    lis.append([name,score])

    lis.sort(key=lambda lis:lis[1])
    print(lis)
second_low = []
for i in range(len(lis)):
    if lis[i][1]  != lis[0][1]: #37.2 # lis[i][1] 37.2,37.21,37.21,39.0,41.0
        second_low.append(lis[i][0])
        for j in range(i+1,len(lis)):
            if lis[j][1] == lis[i][1]:
                second_low.append(lis[j][0])
                print(second_low)
            else:
                break
        break

    else:
        continue
second_low.sort()
for i in second_low:
    print(i)
