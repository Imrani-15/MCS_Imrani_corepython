'''
Types of Methods
----------------
Instance Method
Class Method
Static Method


INSTANCE METHOD
---------------
Inside method implementation if we are using instance variable inside a methods then such type of methods
also called as Instance Method
Inside instance method we can pass the self variable like that def m1(self):
within the class we can call instance method by using self variable and from outside by using the object reference
variable

SETTER METHOD AND GETTER METHOD
------------------------------
SETTER METHOD
------------
Setter method we can set the instance variable by using the setter

syntax
------
def setVariable(self):
    self.Variable = Variable

GETTER METHOD
------------
Getter method we can get the instance variable by using the getter

syntax:
------
def getVariable(self):
    return self.variable

CLASS METHOD
-----------

Inside method implementation only we can use cls variable (static variable) such type of Methods is called
as class method
we can declare the class method exiplicity by using @classmethod decoration
we can declare the class method we should pass the cls variable at the time declration
we can call the class method by using class name or object reference number

Example:
------
class Book:
    pages = 200
    @classmethod
    def book(cls,name):
        print("{} book have the {} pages".format(name,Book.pages))
b = Book()
b.book('Winner')

STATIC METHOD:
-------------
Static method we are using the general purpose
Inside this method we won't use the instance variable and cls variable
We can use the static method exiplicity @staticmethod decorator
we can access the static method by using the class name or object reference

Example:
--------
class Name:
    @staticmethod
    def add(a,b):
        print(a+b)
Name.add(10,20)


PASSING MEMBERS OF ONE CLASS TO ANOTHER CLASS:
---------------------------------------------
We can access the one class to inside another class

Example:
------

class Employee:
    def __init__(self,Emp_Id,Name,Esal):
        self.Emp_Id = Emp_Id
        self.Name = Name
        self.Esal = Esal
    def display(self):
        print("Emploaye id number:",self.Emp_Id)
        print("Emploaye Name:",self.Name)
        print("Emploaye Employee salary:",self.Esal)
class Inc_sal:
    def modify(self):
        self.Esal = self.Esal+1000
        e.display()
e = Employee('0087','john',10000)
Inc_sal.modify(e)
'''

'''
INHERITANCE
-----------

what ever have variable, methods and constructors in parent class we can inharitant the child class also 
main advantage of inheritance code reuseability


TYPES OF INHERITANCE
--------------------
1 Single Inheritance 
2 Multi Level Inheritance
3 Hierarchical Inheritance
4 Multiple Inheritance
5 Hybrid Inheritance

Syntax Example:
---------------
class Baseclass:
    base_class_body
class deriveclass(Baseclass):
    derive_class_body
    
Program on Inheritance:
----------------------
class Animal:
    def eating(self):
        print("eating")
class Dog(Animal):
    def legs(self):
        print("animal have the 4 legs")
d = Dog()
d.eating()
d.legs()


SUPER() METHOD
--------------
super() method is a build-in-method which is usefull to call the super class constructor,variable,methods from the 
child class
'''
'''
ENCAPSULATION
-------------
Encapsulation is one of the fundamental topic in oops concept.It describes the idea of wrapping data 
and the methods that work on data within one unit.

'''
