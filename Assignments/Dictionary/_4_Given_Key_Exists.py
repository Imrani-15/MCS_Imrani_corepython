class Key:
    def __init__(self,dict):
        self.dict = dict
    def check(self,dict,key):
        self.dict = dict
        self.key = key
        if key in dict:
            print("present",end=" ")
            print("value =",dict[key])
        else:
            print("not present")
dict = {'a': 100, 'b':200, 'c':300}
key = input("enter your key:")
k = Key(dict)
k.check(dict,key)