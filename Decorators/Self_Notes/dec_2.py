def create_add(x):
    def adder(y):
        return x+y
    return adder
res = create_add(10)
print(res(15))