# compute sum of digits of a given string
def sum_digits(str1):
    sum_digit = 0
    for i in str1:
        if i.isdigit() == True:
            num = int(i)
            sum_digit = sum_digit+num
    print("Sum of digits of a give string: ",sum_digit)
str1 = input("Enter the string with numbers: ")
sum_digits(str1)