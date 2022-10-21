# that accepts a string and calculate the number of digits and letters
str1 = input("Enter the String with numbers: ")
letter=digits=0
for i in str1:
    if i.isdigit():
        digits = digits+1
    elif i.isalpha():
        letter = letter+1
    else:
        pass
print("Showing the letter in the string:",letter)
print("Showing the number in the string: ",digits)