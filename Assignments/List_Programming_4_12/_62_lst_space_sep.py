# Print a list of space-separated elements
lst = input("Enter your list here:").split(",")
res = []
for i in lst:
    res.append(i)
print("List of space-separated elements: "," ".join(list(res)))
print(type(res))


