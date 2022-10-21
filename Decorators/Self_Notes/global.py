'''x = 10 #Global variable
def func():
    print("Global variable: ",x)
func()


x = 10
def func():
    res = x+1
    print("Modifing global variable inside local scope: ",res) # we will get the error here
func()

y = 10  # golbal variable
print("Out side function global variable: ", y)
def func():
    x = 20  # local variable
    global y
    res = x + y
    print("Inside the function: ", res)
    y = y + 1
    print("Modify the global variable inside the function: ", y)
func()
print("outSide function modify global variable:", y)





'''