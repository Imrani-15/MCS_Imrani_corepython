class Element:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def sum_of_element(self,res):
        self.res = res
        print("First number:",self.num1)
        print("Second number:",self.num2)
        print("Sum of the two elements:",res)
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
e = Element(num1,num2)
res = e.num1+e.num2
e.sum_of_element(res)