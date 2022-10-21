# y = 10 # Global variable
# def outer(): #Enclosing Function
#     z = 4 # Enclosed variable
#     def inner(): #Nested Function
#         x = 5
#         print("X:",x)
#         print("Inside the function global variable: ",y)
#     inner()
#     print("Enclosing variable: ",z)
# outer()


#Modifing the enclosed variable inside the local scope
'''
y = 10
def outer():
    z = 15
    def inner():
        x = 4
        nonlocal z
        z = z+1
        print("Local variable: ",x)
        print("Inside the function enclosed variable: ",z)
    inner()
    print("Outer function enclosed variable: ",z)
outer()

'''


def outer():
    print("start f()")
    def inner():
        print("start g()")
        print("End g()")
        return
    inner()
    print("End f()")
    return
outer()