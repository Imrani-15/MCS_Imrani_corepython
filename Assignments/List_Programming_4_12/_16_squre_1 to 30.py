# First,Last elements whose square value is between 1 and 30
def first_last_ele():
    lst1 = []
    for i in range(1,31):
        lst1.append(i**2)
    print("Square value is between 1 and 30:",lst1)

# First,Last elements whose square value is between 1 and 30,except first 5
    print("Square value is between 1 and 30 except first 5 value:",lst1[5:])


first_last_ele()

