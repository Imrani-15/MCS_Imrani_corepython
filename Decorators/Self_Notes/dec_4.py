def add_decor(func):
    def inner(a,b):
        if a>b:
            print(a*b)
        else:
            func(a,b)
    return inner

@add_decor
def add(a,b):
    print(a+b)
a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
add(a,b)