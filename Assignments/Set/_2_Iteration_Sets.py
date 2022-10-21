class Iteration:
    def __init__(self,test):
        self.test = test
    def loop(self):
        for i in test:
            print(i)
test = set("this is MCS software company")
i = Iteration(test)
i.loop()
