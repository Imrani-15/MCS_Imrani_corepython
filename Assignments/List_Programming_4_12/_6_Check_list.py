# Check list is empty or not
class Check:
    def __init__(self):
        pass
    def empty_or_not(self):
        if len(lst) == 0:
            print("Empty list")
        else:
            print("The List is not Empty")
lst = [10,20,30]
c  = Check()
c.empty_or_not()