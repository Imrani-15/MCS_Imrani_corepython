# Map two lists into a dictionary python
books = ['maths','physics','english']
quntity = [20,50,60]

for i,j in zip(books,quntity):
    print(i,j)


result = dict(zip(books,quntity))
print("Map two lists into a dictionary: ",result)

