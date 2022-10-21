class Employee:
    def __init__(self,Id,Name,Address,Salary):
        self.Id = Id
        self.Name = Name
        self.Address = Address
        self.Salary = Salary
    def details(self):
        print("Employee Id:",self.Id)
        print("Employee Name:",self.Name)
        print("Employee Address:",self.Address)
        print("Employee Salary:",self.Salary)
Id = int(input("Enter your Employee Id:"))
Name = input("Enter your Employee Name:")
Address = input("Enter your Employee Address:")
Salary = float(input("Enter Employee Salary:"))
emp = Employee(Id,Name,Address,Salary)
emp.details()
