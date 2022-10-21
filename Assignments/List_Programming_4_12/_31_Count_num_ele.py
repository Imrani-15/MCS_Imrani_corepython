# Counting number elements within a specified ranges
def get_no_of_elements(lst):
    count = 0
    for i in lst:
        count = count+1
    return count
lst = [10,20,50,'ram',0,None]
print("Counting number elements within a specified ranges:",get_no_of_elements(lst))
