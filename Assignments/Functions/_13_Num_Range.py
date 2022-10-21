# check whether a number is in a given range
class Num_range:
    def __init__(self):
        pass
    def test_range(self,a):
        self.a = a
        if a in range(0,10):
            print( " %s is in the range"%str(a))
        else:
            print("The number is outside the given range.")
n = Num_range()
n.test_range(11)