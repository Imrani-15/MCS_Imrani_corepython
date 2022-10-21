class Max:
    def __init__(self):
        print("this is constructor:")
    def max_three(self,n1,n2,n3):
        if n1>=n2 and n1>=n3:
            print("n1 is the maxmimum value:",n1)
        elif n2>=n3 and n2>=n3:
            print("n2 is the maxmimum value:",n2)
        else:
            print("n3 is the maximum value",n3)
n1 = int(input("Enter your first value:"))
n2 = int(input("Enter your second value:"))
n3 = int(input("Enter your third value:"))
m = Max()
m.max_three(n1,n2,n3)