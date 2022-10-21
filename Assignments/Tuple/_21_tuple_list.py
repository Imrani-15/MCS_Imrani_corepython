#  replace last value of tuples in a list
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print("Replace last value of tuple in a list: ",[t[:-1]+(50,) for t in l])
