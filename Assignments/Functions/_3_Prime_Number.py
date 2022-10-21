def prime_num(start,end):
    for i in range(start,end+1):
        if i>1:
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                print(i)
start = int(input("Enter your starting number:"))
end = int(input("enter your ending number:"))
prime_num(start,end)