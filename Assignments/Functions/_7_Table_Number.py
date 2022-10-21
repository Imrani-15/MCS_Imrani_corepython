def table(num):
    print("The Multiplication table:",num)
    for i in range(1,count+1):
        print(num,'X',i,'=',num*i)
num = int(input("enter your number:"))
count = int(input("Enter upto which number you can calculate:"))
table(num)

