'''
In oops concept the three  important terms of OOP's
1. class
2. Object
3. Reference variable
'''

'''
class
=====
A class is nothing but a blue print
class is represent data members and behaviour of object
HOW TO DEFINE A CLASS
===================
class ClassName:
    "documentation string"
variable: instance variable, static variable, local variable
Methods: instance method, static method
object
======
A physical existance of a class or an instance of a class
we can create any number of objects for a class

Reference variable
=================
The variable which can be used to refer object is called as reference variable
An object can have multiple reference variable
'''
'''
# MAIN CONCEPTS OF OBJECT-ORIENCTED PROGRAMMING (OOPs)
* Class
* Object
* Polymorphism

==============

* Encapsulation
===============
 Encapsulation refer to wrapping of data under a single unit

 Benfits of Encapsulation
 ========================
 Data Hiding
 Flexibility
 Reusability
 
* Inheritance
'''



class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

s = Student("john",101)
# s is reference variable at the same time object also
# Student("john",101) is a object
print(s.name)
print(s.rollno)
