# Create a list by concatenating a given list which range goes from 1 to n
my_list = input("Enter your list: ").split(",")
n = int(input("Enter your number:"))
new_list = ["{}{}".format(x,y) for y in range(1,n+1) for x in my_list]
print(new_list)