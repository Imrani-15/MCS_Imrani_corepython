class Student:
    def __init__(self,sub1,sub2,sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    def details(self):
        print("\nFirst subject Name:",self.sub1)
        print("Second subject Name:",self.sub2)
        print("Third subject Name:",self.sub3)
        print("Fourth subject Name:",self.sub4)
sub1 = input("Enter First Subject:")
sub2 = input("Enter Second Subject:")
sub3 = input("Enter Third Subject:")
s = Student(sub1,sub2,sub3)
s.sub4 = input("Enter fourth subject:")
s.details()