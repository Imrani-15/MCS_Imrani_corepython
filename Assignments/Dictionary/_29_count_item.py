# Count number of items in a dictionary value that is a list
d = { 'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'B' : 34,
        'C' : 12,
        'D' : [7, 8, 9, 6, 4] }
count = 0
for key,value in d.items():
        if isinstance(value,list):
                count = count+len(value)
print("count number if items in a dict: ",count)
