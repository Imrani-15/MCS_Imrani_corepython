class Person:
    def __init__(self,Name,Phonenumber):
        self.Name = Name
        self.Phonenumber = Phonenumber
    def details(self):
        print("My name is {}".format(self.Name))
        print("My Phone Number is {}".format(self.Phonenumber))
Name = input("Enter Your Name:")
Phonenumber = int(input("Enter your phonenumber"))
p = Person(Name,Phonenumber)
p.details()