# find the first repeated word in a given string
from collections import Counter
def first_repeated(str1):
    count = {}
    res = []
    words = str1.split(' ')
    for word in words:
        if word in count:
            count[word] = count[word]+1
            print(count)
        else:
            count[word] = 1
            res.append(word)
    for word in res:
        if count[word] != 1:
            return word
    return None
str1 = input("Enter your string here:")
print("first repeated word in a given string:",first_repeated(str1))
