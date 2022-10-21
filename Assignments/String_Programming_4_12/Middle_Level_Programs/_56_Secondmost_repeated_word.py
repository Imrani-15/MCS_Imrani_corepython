# find the second most repeated word in a given string
def second_repeated(str1):
    count = dict()
    res = []
    words = str1.split(' ')
    for word in words:
        if word in count:
            count[word] = count[word]+1
            print(count)
        else:
            count[word] = 1
            res.append(word)
            print(res)
    for val in count.values():
        if val == 2:
            print("The second most repeated word in a given string:",val)
    return None
str1 = input("Enter your string:")
second_repeated(str1)