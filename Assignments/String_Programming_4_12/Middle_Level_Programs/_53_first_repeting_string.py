# find the first repeated character in a given string

def repeating(str1):
    char_order = []
    count = {}
    for char in str1:
        if char in count:
            count[char] = count[char]+1
            print(count)
        else:
            count[char] = 1
            char_order.append(char)
    for char in char_order:
        if count[char] != 1:
            return char
    return None
str1 = input("Enter your string")
print("Non Repeating character in given string:",repeating(str1))