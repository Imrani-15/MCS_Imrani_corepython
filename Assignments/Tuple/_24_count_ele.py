#  count the elements in a list until an element is a tuple
def count_ele(li):
    count = 0
    for num in li:
        if isinstance(num,tuple):
            break
        count = count+1
    return count
li = [4, 5, 6, 10, (1, 2, 3), 11, 2, 4]
print(count_ele(li))
