# def decor(func):
#     def inner(a,b):
#         if a>20:
#             print("In Decorators",a+(b+a))
#         else:
#             func()
#     return inner
# #@decor
# def product_get(a,b):
#     print("Main function: ",a//b)
# a = int(input("Enter your a number: "))
# b = int(input("Enter your b number: "))
# res = decor(product_get(a,b))
# res(a,b)

# print("initially:",dir())
# num = 20
# def f1():
#     n = 10
#     print("inside the function:",dir())
# f1()
# print("outside the function:",dir())
# x = 10 #Global variable
# def func():
#     print("Global variable: ",x)
# func()

