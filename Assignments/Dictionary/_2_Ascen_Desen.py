import operator
class Ascen_Desen:
    def __init__(self,dict):
        self.dict = dict
    def value(self):
        ascen = dict(sorted(d.items(),key=operator.itemgetter(1)))
        print(ascen)
        desen = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
        print(desen)
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
a = Ascen_Desen(dict)
a.value()