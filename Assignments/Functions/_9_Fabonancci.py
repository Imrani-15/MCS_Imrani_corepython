class Fabonacci:
    def __init__(self):
        print("This is constructor:")
    def series(self):
        first = 0
        second = 1
        if n<0:
            print("Incorrect input")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(1,n):
                result = first + second # 0+1, 1+1
                first = second
                second = result
            print(second)
n = int(input("Enter how many numbers you want in this series:"))
f = Fabonacci()
f.series()