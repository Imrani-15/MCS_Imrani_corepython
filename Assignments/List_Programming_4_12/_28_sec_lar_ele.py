# Finding a second largest number

def find_len(lst):
    length = len(lst)
    lst.sort()
    print("Largest Element in the List:",lst[length-1]) #lst[-1]
    print("Smallest Element in the List:",lst[0])
    print("Largest Element in the List:",lst[length-2]) #lst[-2]
    print("Smallest Element in the List:",lst[1])
lst = [12, 55, 0, 41, 321, 10, 8, 6, 4]
find_len(lst)