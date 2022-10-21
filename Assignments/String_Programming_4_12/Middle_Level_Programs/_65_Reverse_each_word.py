# Reverse each word in given string Input
def reverse_each_word():
    word = rev_str.split(' ')
    newword = [word[::-1] for word in word]
    new_str = "".join(newword)
    print("New string: ",new_str)
rev_str = input("Enter the string:")
reverse_each_word()