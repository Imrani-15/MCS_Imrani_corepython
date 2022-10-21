def even_Odd(num):
    print("print even numbers")
    for i in range(num):
        if i%2==0:
            print(i,end=" ")
    else:
        print("\n","print odd numbers")
        for j in range(num):
            if j%2!=0:
                print(j,end=" ")
num = int(input("enter your numbre:"))
even_Odd(num)