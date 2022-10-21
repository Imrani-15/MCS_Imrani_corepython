def factorial(num):
    temp = 1
    if num<0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num==0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num+1):
            temp = temp*i
        print("The factorial of",num,"is",temp)
num = int(input("Enter your number:"))
factorial(num)
