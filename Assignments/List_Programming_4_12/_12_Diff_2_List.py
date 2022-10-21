class Diff:
    def __init__(self):
        print("This is constructor:")
    def two_list(self):
        final = []
        for i in lst1:
            if i not in lst2:
                final.append(i)
        print(final)
lst1 = [10, 15, 20, 25, 30, 35, 40]
lst2 = [25, 40, 35]
d = Diff()
d.two_list()
