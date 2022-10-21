def dev_decor(func):
    def inner(a,b):
        if b == 0:
            print("oops cannot divide")
        else:
            func(a,b)
    return inner
@dev_decor
def divi(a,b):
    print(a/b)
a = int(input("Enter your a number: "))
b = int(input("Enter your b number: "))
divi(a,b)