# print given Pascal's triangle
from math import factorial
class Pascal:
    def __init__(self):
        pass
    def triangle(self):
        n = 5
        for i in range(n):
            for j in range(n-i+1):
                print(end=" ")
            for j in range(i+1):

                print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
            print()
p = Pascal()
p.triangle()