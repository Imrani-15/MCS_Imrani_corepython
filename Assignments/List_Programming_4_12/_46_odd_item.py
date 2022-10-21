# Slect odd items of a list
n = int(input("Enter your number: "))
odd = []
for i in range(n):
    if i%2 != 0:
        odd.append(i)
print("Odd items of list is: ",odd)