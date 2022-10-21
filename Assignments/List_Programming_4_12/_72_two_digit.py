# Two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j
row_num = int(input("Enter the row: "))
col_num = int(input("Enter the column"))
multi_dem = [[0 for col in range(col_num)] for row in range(row_num)]
print(multi_dem)
for row in range(row_num):
    for col in range(col_num):
        multi_dem[row][col] = row*col
print(multi_dem)