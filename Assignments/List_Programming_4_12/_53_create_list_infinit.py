# Create a list with infinite elements
def infinite_ele(n):
    res  = []
    for i in range(n):
        res.append(i)
    return res
n = int(input("Enter inifinite element: "))
print(infinite_ele(n))

