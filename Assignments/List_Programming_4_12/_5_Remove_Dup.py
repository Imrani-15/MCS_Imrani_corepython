class Remove:
    def __init__(self,list):
        self.list = list
    def ele(self):
        result = []
        for i in list:
            if i not in result:
                result.append(i)
        print("Remove the duplicates in list:",result)
list = [1,2,3,3,2,1,5,6,1,5]
r = Remove(list)
r.ele()