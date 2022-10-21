# Words that are longer than any element

def longestlen(lst1):
    max1 = len(lst1[0])
    temp = lst1[0]
    for i in lst1:
        if len(i)> max1:
            max1 = len(i)
            temp = i
    print("The word with the longest lenght is ",temp,"and length is",max1)
lst1 = ['pavani','johny','sireesha','sowjanya']
longestlen(lst1)