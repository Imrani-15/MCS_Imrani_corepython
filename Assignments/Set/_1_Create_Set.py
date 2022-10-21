class Create:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def set(self):
        final = self.a, self.b
        print(set(final))
c = Create(10,20)
c.set()

