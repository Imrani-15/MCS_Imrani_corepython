def deccor(func):
    def inner(name):
        if name == "Ravi":
            print("Hello Ravi have a great day")
        else:
            func(name)
    return inner
@deccor
def wish(name):
    print("hello",name,"Good Morning")
wish("Ravi")

