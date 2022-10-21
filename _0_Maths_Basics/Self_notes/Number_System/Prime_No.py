# def isPrime(n):
#     # since 0 and 1 is not prime return false
#     if (n==1 or n==0):
#         return False
#     for i in range(2,n):
#         # if the number is divisible by i, then n is not a prime number.
#         if n%i==0:
#             return False
#     return True
# n = 10
# print(isPrime(n))

# num = 10
# for i in range(1, num+1):
#     if(isPrime(i)):
#         print(i,end=" ")

'''
Sine 1 and 0 is not prime numbers
If number is divisiable 2 then numbers is not prime number
All prime numbers greater than one
# '''

# start_no = int(input("Enter your start_no:"))
# End_no = int(input("Enter your End_no:"))
# for i in range(start_no, End_no+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)
