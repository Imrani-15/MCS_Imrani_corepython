class Computer:
    def __init__(self,brand,price,version):
        self.brand = brand
        self.price = price
        self.version = version
    def display(self):
        print("\nYour system brand is: {}".format(self.brand))
        print("Your system price is: {}".format(self.price))
        print("Your system version is: {}".format(self.version))
brand = input("Enter your system brand name:")
price = input("Enter your system price:")
version = input("Enter your system version: ")
c = Computer(brand,price,version)
c.display()
