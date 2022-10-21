class Add_Key(dict):
    def __init__(self):
        self = dict()
    def final(self,key,value):
        self[key] = value
a = Add_Key()
a.final(1,'one')
a.final(2,'two')
print(a)
