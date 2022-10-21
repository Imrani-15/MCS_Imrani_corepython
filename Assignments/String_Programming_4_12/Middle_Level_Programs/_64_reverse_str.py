# Reverse a given string  Input : "Python"   Output : "nohtyP"
def rev_str1(str1):
    rev_str = ''
    for char in str1:
        rev_str = char+rev_str
    print(rev_str)
str1 = input("Enter the string: ")
rev_str1(str1)